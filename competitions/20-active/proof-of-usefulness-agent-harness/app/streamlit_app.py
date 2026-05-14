from __future__ import annotations

import json
import sys
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

import streamlit as st
from jsonschema import Draft202012Validator


APP_DIR = Path(__file__).resolve().parent
SRC_DIR = APP_DIR / "src"
SAMPLES_DIR = APP_DIR / "samples"
OUT_DIR = APP_DIR / "out"
RUN_LOG_DIR = APP_DIR / "run-logs"
SCHEMA_PATH = APP_DIR / "schema" / "competition-card.schema.json"

sys.path.insert(0, str(SRC_DIR))
from harness import build_card  # noqa: E402


st.set_page_config(
    page_title="AI 机会可行性与执行助手",
    layout="wide",
)

st.markdown(
    """
    <style>
    [data-testid="stToolbar"] { visibility: hidden; height: 0; }
    [data-testid="stDecoration"] { display: none; }
    .stMetric { border: 1px solid #e5e7eb; border-radius: 8px; padding: 12px; background: #fafafa; }
    </style>
    """,
    unsafe_allow_html=True,
)


def load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def list_samples() -> list[Path]:
    return sorted(SAMPLES_DIR.glob("*.md"))


def load_sample_text(sample_name: str) -> str:
    samples = {path.name: path for path in list_samples()}
    return samples[sample_name].read_text(encoding="utf-8")


def validate_card(card: dict) -> list[str]:
    validator = Draft202012Validator(load_schema())
    return [error.message for error in sorted(validator.iter_errors(card), key=str)]


def save_outputs(card: dict, markdown: str) -> tuple[Path, Path]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    RUN_LOG_DIR.mkdir(parents=True, exist_ok=True)
    slug = card["name"].lower()
    for old, new in ((" ", "-"), (":", ""), ("/", "-"), ("&", "and")):
        slug = slug.replace(old, new)
    slug = "".join(ch for ch in slug if ch.isalnum() or ch in "-_")[:80].strip("-") or "competition"
    output_path = OUT_DIR / f"{slug}.ui.json"
    output_path.write_text(json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    log_path = RUN_LOG_DIR / f"{timestamp}-ui.md"
    log_path.write_text(
        "\n".join(
            [
                f"# UI 运行日志：{card['name']}",
                "",
                f"- 时间：{timestamp}",
                f"- 来源：{card['source_url']}",
                f"- 建议：{card['recommendation']}",
                f"- 8GB：{card['fit_8gb']}",
                "",
                "## 输入",
                "",
                "```markdown",
                markdown,
                "```",
                "",
                "## 输出",
                "",
                "```json",
                json.dumps(card, ensure_ascii=False, indent=2),
                "```",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return output_path, log_path


def recommendation_label(value: str) -> str:
    labels = {
        "active": "主线推进",
        "candidate": "候选",
        "watchlist": "观察",
        "rejected": "排除",
        "reference": "仅参考",
    }
    return labels.get(value, value)


def render_card(card: dict, validation_errors: list[str]) -> None:
    st.subheader(card["name"])

    left, mid, right, last = st.columns(4)
    left.metric("建议", recommendation_label(card["recommendation"]))
    mid.metric("参赛资格", card["eligibility"])
    right.metric("8GB 可行性", card["fit_8gb"])
    last.metric("时间窗口", card["deadline_or_window"])

    if validation_errors:
        st.error("Schema 校验未通过")
        for error in validation_errors:
            st.write(f"- {error}")
    else:
        st.success("Schema 校验通过")

    risk_col, plan_col = st.columns(2)
    with risk_col:
        st.markdown("#### 风险与人工复核点")
        for risk in card["risks"]:
            st.warning(risk)

    with plan_col:
        st.markdown("#### 48 小时行动计划")
        for index, item in enumerate(card["next_48h_plan"], start=1):
            st.write(f"{index}. {item}")

    st.markdown("#### 证据片段")
    for item in card["evidence"]:
        st.code(item, language="text")

    st.markdown("#### JSON 输出")
    st.json(card)


def main() -> None:
    st.title("AI 机会可行性与执行助手")
    st.caption("把 hackathon、bounty、比赛规则或内部 AI idea 转成可复核的资源判断、风险和执行计划。")

    samples = list_samples()
    if not samples:
        st.error("未找到 samples 目录中的 Markdown 样例。")
        return

    with st.sidebar:
        st.header("输入")
        sample_names = [path.name for path in samples]
        selected = st.selectbox("选择真实机会样例", sample_names, index=sample_names.index("proof-of-usefulness.md") if "proof-of-usefulness.md" in sample_names else 0)
        if st.button("载入样例", use_container_width=True):
            st.session_state["markdown"] = load_sample_text(selected)
        st.divider()
        st.markdown("**当前提交目标**")
        st.write("Proof of Usefulness")
        st.write("\\$20k cash + \\$130k+ software credits")
        st.write("截止：2026-06-05")

    if "markdown" not in st.session_state:
        st.session_state["markdown"] = load_sample_text(selected)

    markdown = st.text_area(
        "机会说明 / 规则 / 证据 Markdown",
        value=st.session_state["markdown"],
        height=360,
        help="可以粘贴官网规则、需求说明、提交要求、资格说明和本地约束。",
    )
    st.session_state["markdown"] = markdown

    card = asdict(build_card(markdown))
    validation_errors = validate_card(card)

    action_col, save_col = st.columns([1, 1])
    with action_col:
        st.button("重新分析", use_container_width=True)
    with save_col:
        if st.button("保存 JSON 和运行日志", use_container_width=True):
            output_path, log_path = save_outputs(card, markdown)
            st.success(f"已保存：{output_path.name} / {log_path.name}")

    render_card(card, validation_errors)


if __name__ == "__main__":
    main()

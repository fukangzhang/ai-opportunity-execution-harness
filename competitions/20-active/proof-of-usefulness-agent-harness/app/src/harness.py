from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


ELIGIBILITY_VALUES = {"开放参赛", "企业/组织限定", "邀请制", "未知"}
FIT_VALUES = {"A 本地可做", "B API/云端", "C 平台 Notebook", "D 不建议主攻"}


@dataclass
class CompetitionCard:
    name: str
    source_url: str
    eligibility: str
    deadline_or_window: str
    fit_8gb: str
    recommendation: str
    risks: list[str]
    next_48h_plan: list[str]
    evidence: list[str]


def read_markdown(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def first_heading(markdown: str) -> str:
    match = re.search(r"^#\s+(.+)$", markdown, re.MULTILINE)
    return match.group(1).strip() if match else "Untitled Competition"


def source_url(markdown: str) -> str:
    match = re.search(r"Source:\s*(https?://\S+)", markdown)
    return match.group(1).strip() if match else "https://example.invalid/"


def deadline_or_window(markdown: str) -> str:
    for label in ("Rolling Submissions", "Window"):
        match = re.search(label + r":\s*([^\n]+)", markdown)
        if match:
            return match.group(1).strip().rstrip(".")
    return "未知"


def infer_eligibility(markdown: str) -> str:
    lower = markdown.lower()
    if "student" in lower and ("only" in lower or "限定" in markdown):
        return "未知"
    if "invitation" in lower or "邀请" in markdown:
        return "邀请制"
    if "company" in lower and "required" in lower:
        return "企业/组织限定"
    if "open to everyone" in lower or "individual developers" in lower or "open competition" in lower:
        return "开放参赛"
    return "未知"


def infer_8gb_fit(markdown: str) -> str:
    lower = markdown.lower()
    if "8gb" in lower and any(word in lower for word in ("cpu", "lightgbm", "sklearn", "tabular")):
        return "A 本地可做"
    if any(word in lower for word in ("api/cloud", "api", "cloud", "sponsor technologies")):
        return "B API/云端"
    if "notebook" in lower or "kaggle" in lower:
        return "C 平台 Notebook"
    if any(word in lower for word in ("multi-gpu", "large gpu", "专用硬件")):
        return "D 不建议主攻"
    return "B API/云端"


def infer_recommendation(markdown: str, fit_8gb: str) -> str:
    lower = markdown.lower()
    if "do not make it active" in lower or "reference only" in lower or "lock-in" in lower:
        return "reference"
    if "student only" in lower or fit_8gb == "D 不建议主攻":
        return "rejected"
    if "second active" in lower or "active line" in lower:
        return "active"
    if "proof of usefulness" in lower:
        return "active"
    return "candidate"


def collect_risks(markdown: str) -> list[str]:
    lower = markdown.lower()
    risks: list[str] = []
    if "sponsor technologies" in lower:
        risks.append("大奖可能偏向 sponsor technologies，需要避免核心架构被赞助商生态锁死。")
    if "copilot studio" in lower or "low-code" in lower or "lock-in" in lower:
        risks.append("生态绑定较强，复用价值低，默认只作反例或参考。")
    if "github repo" in lower and "live project url" in lower:
        risks.append("提交前必须准备 live URL、公开代码仓库和可验证的使用证据。")
    if not risks:
        risks.append("提交前需要复核完整官方规则、资格和交付物。")
    return risks


def next_plan(recommendation: str) -> list[str]:
    if recommendation == "active":
        return [
            "整理官方规则证据，确认资格、截止时间、交付字段。",
            "定义最小数据 schema，并准备 3 个真实比赛样例。",
            "实现 Markdown 输入到结构化比赛卡片的本地闭环。",
            "记录人工复核点和失败样例，为 PoU 证据做准备。",
        ]
    if recommendation == "reference":
        return [
            "保留来源和排除原因。",
            "抽取可借鉴的评分项和材料结构。",
            "验证系统能识别生态绑定风险并降级处理。",
        ]
    return [
        "补齐资格、截止时间、来源和 8GB 可行性。",
        "决定进入 candidate、watchlist 或 rejected。",
    ]


def extract_evidence(markdown: str) -> list[str]:
    evidence: list[str] = []
    for line_number, line in enumerate(markdown.splitlines(), start=1):
        text = line.strip()
        if not text:
            continue
        if any(key in text.lower() for key in ("source:", "window:", "rolling submissions", "open", "8gb", "requires", "decision note", "audience:", "submission requires")):
            evidence.append(f"L{line_number}: {text}")
    return evidence[:8]


def build_card(markdown: str) -> CompetitionCard:
    fit = infer_8gb_fit(markdown)
    recommendation = infer_recommendation(markdown, fit)
    eligibility = infer_eligibility(markdown)
    if eligibility not in ELIGIBILITY_VALUES:
        eligibility = "未知"
    if fit not in FIT_VALUES:
        fit = "B API/云端"
    return CompetitionCard(
        name=first_heading(markdown),
        source_url=source_url(markdown),
        eligibility=eligibility,
        deadline_or_window=deadline_or_window(markdown),
        fit_8gb=fit,
        recommendation=recommendation,
        risks=collect_risks(markdown),
        next_48h_plan=next_plan(recommendation),
        evidence=extract_evidence(markdown),
    )


def write_card(card: CompetitionCard, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(asdict(card), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run_one(input_path: Path, output_path: Path) -> None:
    card = build_card(read_markdown(input_path))
    write_card(card, output_path)
    print(f"Wrote {output_path}")


def run_all_samples(app_dir: Path) -> None:
    samples_dir = app_dir / "samples"
    out_dir = app_dir / "out"
    for input_path in sorted(samples_dir.glob("*.md")):
        run_one(input_path, out_dir / (input_path.stem + ".json"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="生成比赛结构化卡片")
    parser.add_argument("--input", type=Path, help="输入 Markdown 文件")
    parser.add_argument("--output", type=Path, help="输出 JSON 文件")
    parser.add_argument("--all-samples", action="store_true", help="批量处理 samples 目录")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    app_dir = Path(__file__).resolve().parents[1]
    if args.all_samples:
        run_all_samples(app_dir)
        return
    if not args.input or not args.output:
        raise SystemExit("请提供 --input 和 --output，或使用 --all-samples。")
    run_one(args.input, args.output)


if __name__ == "__main__":
    main()

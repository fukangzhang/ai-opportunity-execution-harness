const sampleSelect = document.querySelector("#sample-select");
const briefInput = document.querySelector("#brief-input");
const analyzeButton = document.querySelector("#analyze-button");
const downloadButton = document.querySelector("#download-button");

let currentCard = null;

const ELIGIBILITY_VALUES = new Set(["开放参赛", "企业/组织限定", "邀请制", "未知"]);
const FIT_VALUES = new Set(["A 本地可做", "B API/云端", "C 平台 Notebook", "D 不建议主攻"]);

function firstHeading(markdown) {
  const match = markdown.match(/^#\s+(.+)$/m);
  return match ? match[1].trim() : "Untitled Opportunity";
}

function sourceUrl(markdown) {
  const match = markdown.match(/Source:\s*(https?:\/\/\S+)/);
  return match ? match[1].trim() : "https://example.invalid/";
}

function deadlineOrWindow(markdown) {
  for (const label of ["Rolling Submissions", "Window"]) {
    const match = markdown.match(new RegExp(`${label}:\\s*([^\\n]+)`));
    if (match) return match[1].trim().replace(/\.$/, "");
  }
  return "未知";
}

function inferEligibility(markdown) {
  const lower = markdown.toLowerCase();
  if (lower.includes("student") && (lower.includes("only") || markdown.includes("限定"))) return "未知";
  if (lower.includes("invitation") || markdown.includes("邀请")) return "邀请制";
  if (lower.includes("company") && lower.includes("required")) return "企业/组织限定";
  if (lower.includes("open to everyone") || lower.includes("individual developers") || lower.includes("open competition")) {
    return "开放参赛";
  }
  return "未知";
}

function infer8gbFit(markdown) {
  const lower = markdown.toLowerCase();
  if (lower.includes("8gb") && ["cpu", "lightgbm", "sklearn", "tabular"].some((word) => lower.includes(word))) {
    return "A 本地可做";
  }
  if (["api/cloud", "api", "cloud", "sponsor technologies"].some((word) => lower.includes(word))) {
    return "B API/云端";
  }
  if (lower.includes("notebook") || lower.includes("kaggle")) return "C 平台 Notebook";
  if (["multi-gpu", "large gpu", "专用硬件"].some((word) => lower.includes(word))) return "D 不建议主攻";
  return "B API/云端";
}

function inferRecommendation(markdown, fit8gb) {
  const lower = markdown.toLowerCase();
  if (lower.includes("do not make it active") || lower.includes("reference only") || lower.includes("lock-in")) return "reference";
  if (lower.includes("student only") || fit8gb === "D 不建议主攻") return "rejected";
  if (lower.includes("second active") || lower.includes("active line")) return "active";
  if (lower.includes("proof of usefulness")) return "active";
  return "candidate";
}

function collectRisks(markdown) {
  const lower = markdown.toLowerCase();
  const risks = [];
  if (lower.includes("sponsor technologies")) {
    risks.push("大奖可能偏向 sponsor technologies，需要避免核心架构被赞助商生态锁死。");
  }
  if (lower.includes("copilot studio") || lower.includes("low-code") || lower.includes("lock-in")) {
    risks.push("生态绑定较强，复用价值低，默认只作反例或参考。");
  }
  if (lower.includes("github repo") && lower.includes("live project url")) {
    risks.push("提交前必须准备 live URL、公开代码仓库和可验证的使用证据。");
  }
  if (!risks.length) risks.push("提交前需要复核完整官方规则、资格和交付物。");
  return risks;
}

function nextPlan(recommendation) {
  if (recommendation === "active") {
    return [
      "整理官方规则证据，确认资格、截止时间、交付字段。",
      "定义最小数据 schema，并准备 3 个真实比赛样例。",
      "实现 Markdown 输入到结构化比赛卡片的本地闭环。",
      "记录人工复核点和失败样例，为 PoU 证据做准备。",
    ];
  }
  if (recommendation === "reference") {
    return ["保留来源和排除原因。", "抽取可借鉴的评分项和材料结构。", "验证系统能识别生态绑定风险并降级处理。"];
  }
  return ["补齐资格、截止时间、来源和 8GB 可行性。", "决定进入 candidate、watchlist 或 rejected。"];
}

function extractEvidence(markdown) {
  const keys = ["source:", "window:", "rolling submissions", "open", "8gb", "requires", "decision note", "audience:", "submission requires"];
  return markdown
    .split(/\r?\n/)
    .map((line, index) => ({ text: line.trim(), number: index + 1 }))
    .filter(({ text }) => text && keys.some((key) => text.toLowerCase().includes(key)))
    .slice(0, 8)
    .map(({ text, number }) => `L${number}: ${text}`);
}

function buildCard(markdown) {
  let fit8gb = infer8gbFit(markdown);
  if (!FIT_VALUES.has(fit8gb)) fit8gb = "B API/云端";
  let eligibility = inferEligibility(markdown);
  if (!ELIGIBILITY_VALUES.has(eligibility)) eligibility = "未知";
  const recommendation = inferRecommendation(markdown, fit8gb);
  return {
    name: firstHeading(markdown),
    source_url: sourceUrl(markdown),
    eligibility,
    deadline_or_window: deadlineOrWindow(markdown),
    fit_8gb: fit8gb,
    recommendation,
    risks: collectRisks(markdown),
    next_48h_plan: nextPlan(recommendation),
    evidence: extractEvidence(markdown),
  };
}

function fillList(selector, values, ordered = false) {
  const list = document.querySelector(selector);
  list.innerHTML = "";
  for (const value of values) {
    const item = document.createElement("li");
    item.textContent = value;
    list.appendChild(item);
  }
  list.parentElement.hidden = ordered ? false : false;
}

function renderCard(card) {
  currentCard = card;
  document.querySelector("#card-name").textContent = card.name;
  document.querySelector("#recommendation").textContent = card.recommendation;
  document.querySelector("#recommendation").className = `pill ${card.recommendation}`;
  document.querySelector("#eligibility").textContent = card.eligibility;
  document.querySelector("#fit").textContent = card.fit_8gb;
  document.querySelector("#window").textContent = card.deadline_or_window;
  fillList("#risks", card.risks);
  fillList("#plan", card.next_48h_plan, true);
  fillList("#evidence", card.evidence.length ? card.evidence : ["No evidence lines found."]);
}

async function loadSample(name) {
  const response = await fetch(`samples/${name}`);
  if (!response.ok) throw new Error(`Failed to load sample: ${name}`);
  const markdown = await response.text();
  briefInput.value = markdown;
  renderCard(buildCard(markdown));
}

function analyze() {
  renderCard(buildCard(briefInput.value));
}

function downloadJson() {
  if (!currentCard) analyze();
  const blob = new Blob([JSON.stringify(currentCard, null, 2) + "\n"], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = `${currentCard.name.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") || "opportunity-card"}.json`;
  link.click();
  URL.revokeObjectURL(url);
}

sampleSelect.addEventListener("change", () => loadSample(sampleSelect.value));
analyzeButton.addEventListener("click", analyze);
downloadButton.addEventListener("click", downloadJson);

loadSample(sampleSelect.value).catch((error) => {
  briefInput.value = `# Sample failed to load\n\nSource: https://example.invalid/\n\n${error.message}`;
  analyze();
});

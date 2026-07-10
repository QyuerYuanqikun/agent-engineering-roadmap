# Agent Engineering 12 周学习与求职路线

> **文件名固定：** `Agent_Engineering_12_Week_Roadmap.md`
>
> **新版定位：** Hello-Agents 作为“Agent 思维与原理主教材”；LangChain v1 / LangGraph / LangSmith / MCP 官方文档作为“工程主训练”；你的 **Multi-Agent Literature Extraction System（多 Agent 文献结构化抽取系统）**作为贯穿 12 周的唯一主项目；低热水泥 / AI4Materials 文献仅作为可选应用与评测场景，不定义项目身份。
>
> **版本核验日期：** 2026-07-09。Agent 生态变化很快，执行时若 API 有变，以当天官方文档为准。
>
> **时间约束：** 每天最多 3 小时；84 天连续计划；总投入约 210–235 小时。

---

## 0. 这版为什么重构

旧版路线偏“工程框架训练”；新版补上了 Hello-Agents 最有价值的连续认知链：

```text
什么是 Agent
   ↓
ReAct / Plan-and-Solve / Reflection
   ↓
自己实现 Agent Loop
   ↓
自己构建最小 Agent Harness
   ↓
再进入 LangChain v1 / LangGraph
   ↓
Multi-Agent Coordination
   ↓
Evaluation / Tracing / Context / MCP
   ↓
FastAPI / Testing / Docker / Portfolio
```

核心原则：**Hello-Agents 是主教材，不是唯一工程世界观；官方文档与可测项目负责把能力拉到求职水平。**

---

## 1. 12 周 Level 总览

| Level | 周期 | 核心能力 | 主要产出 | 晋级本质 |
|---|---|---|---|---|
| Level 0 | Week 1–2 | Agent 思维 + 经典范式 + 无框架 Loop | `mini-agent + 20-case eval` | 理解 ReAct / Plan-and-Solve / Reflection，并能手写受控 Agent Loop |
| Level 1 | Week 3–4 | 自研 Agent Harness + LangChain v1 | `自研 mini framework + single-agent extractor v1` | 既能造轮子，又能解释现代 Agent harness 的抽象 |
| Level 2 | Week 5–6 | LangGraph 状态化编排 + Persistence + HITL | `paper-extraction-graph-v2` | 能构建可暂停、可恢复、可测试的 stateful agent |
| Level 3 | Week 7–8 | Multi-Agent 协调 + DeepResearch 思维 | `paper-multi-agent-v3 + baseline study` | 能证明何时多 Agent 有价值，何时没有 |
| Level 4 | Week 9–10 | Evaluation + Tracing + Context Engineering + MCP | `eval suite + context ablation + MCP server` | 能用数据和 trace 驱动可靠性改进 |
| Level 5 | Week 11–12 | Production + Portfolio + Interview | `Multi-Agent Literature Extraction System` | 达到可 clone、可运行、可评估、可答辩的求职作品水平 |

### 晋级规则

- Level Gate 是**硬门槛**，不是“看完章节”。
- 任一 Gate 未通过：先修复失败项，再进入下一级。
- 每次验收都必须保留：测试结果、失败样例、Trace/事件记录、复盘文档。
- 所有“提升”必须有 baseline；没有对照实验，不允许宣称多 Agent 更优。

---

## 2. 每天固定执行模板（≤3 h）

```text
35–50 min   阅读指定页面，只做问题导向笔记
80–100 min  独立编码 / 改造主项目
25–35 min   测试、故障注入、Trace 检查
10–20 min   写复盘：今天的架构决策与失败
--------------------------------------
总计         2 h 30 min – 3 h
```

### 每天必须留下的最小证据

1. 一个 commit。
2. 一个可运行产出或可检验笔记。
3. 至少一个测试 / 故障注入 / 闭卷口述结果。
4. `daily-log.md` 追加 3 行：**学到什么、失败什么、下一步验证什么**。

---

## 3. 建议仓库结构

```text
agent-engineering-roadmap/
├── 00-notes/
├── 01-mini-agent-loop/
├── 02-agent-framework/
├── 03-single-agent/
├── 04-langgraph-extractor/
├── 05-multi-agent/
├── 06-evaluation/
├── 07-context-mcp/
├── 08-production-app/
├── datasets/
├── reports/
├── reviews/
├── level-gates/
├── portfolio/
└── README.md
```

---

# Level 0 — Agent 思维 + 经典范式 + 无框架 Loop

**周期：** Week 1–2  
**Level 主要产出：** `mini-agent + 20-case eval`  
**晋级本质：** 理解 ReAct / Plan-and-Solve / Reflection，并能手写受控 Agent Loop

## Week 1 — Agent 边界与经典范式

### Day 1 — Agent、Workflow、Chatbot：先学会“不用 Agent”

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch1](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter1/%E7%AC%AC%E4%B8%80%E7%AB%A0%20%E5%88%9D%E8%AF%86%E6%99%BA%E8%83%BD%E4%BD%93.md)
- [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)

**今天学什么**

- 精读 Ch1 中“智能体定义、环境、行动、自主性、LLM Agent 新范式”相关部分。
- 区分 chatbot / deterministic workflow / agent；理解“自主决策”不等于“无限自治”。
- 用你的真实任务做架构判断，而不是背定义。

**今天动手做什么**

- 对 12 个任务分类：普通函数、Workflow、Single Agent、Multi-Agent。
- 必须包含：文献下载、字段抽取、单位归一化、表格解析、跨段落证据检索、多目标配方优化。

**当天产出**

- `00-notes/day01-agent-boundary.md`

**验收测试 / 通过标准**

- [ ] 闭卷用 3 分钟解释四类系统差异。
- [ ] 12 个任务中至少 10 个能给出“为什么不用更复杂架构”的理由。
- [ ] 对“文献字段抽取”写出一个可证伪的 Agent 适用假设。

### Day 2 — 从 Agent 历史中理解“状态、规划、效用”为什么出现

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch2](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter2/%E7%AC%AC%E4%BA%8C%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E5%8F%91%E5%B1%95%E5%8F%B2.md)
- [Agent Learning Hub](https://github.com/datawhalechina/Agent-Learning-Hub)

**今天学什么**

- 快速阅读 Ch2，不追求历史细节；重点抓“上一代范式解决什么问题，又产生什么新问题”。
- 理解反射式、基于模型、目标式、效用式、学习型 Agent。
- 把“内部状态 / 目标 / 规划 / 反馈”映射到现代 LLM Agent。

**今天动手做什么**

- 画一张“传统 Agent → LLM Agent”能力演化图。
- 为文献抽取系统写 5 个状态变量和 3 个目标函数示例。

**当天产出**

- `00-notes/day02-agent-evolution.md` + 1 张 Mermaid 图

**验收测试 / 通过标准**

- [ ] 不看资料解释：为什么仅靠 prompt 不等于 Agent。
- [ ] 能说明“状态”和“聊天历史”为什么不是同一概念。

### Day 3 — LLM 基础只补 Agent 相关缺口：结构化输出与工具选择

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch3](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter3/%E7%AC%AC%E4%B8%89%E7%AB%A0%20%E5%A4%A7%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%E5%9F%BA%E7%A1%80.md)
- [LangChain Structured Output](https://docs.langchain.com/oss/python/langchain/structured-output)

**今天学什么**

- Ch3 只快速读：LLM 局限、提示、API 调用；跳过你已掌握的 Transformer 细节。
- 理解自由文本、JSON、Schema-validated output 的可靠性差异。
- 理解模型“选择工具”和代码“执行工具”是两层职责。

**今天动手做什么**

- 定义 Pydantic 模型 `ExtractionResult`：字段值、单位、证据、置信度、缺失原因。
- 手写 10 个非法输出样例，验证 Schema 能拒绝它们。

**当天产出**

- `01-mini-agent-loop/schemas.py` + `tests/test_schema.py`

**验收测试 / 通过标准**

- [ ] `pytest` 至少 10 条非法样例全部被拒绝。
- [ ] 不能用“让模型自觉输出 JSON”替代验证。

### Day 4 — ReAct：第一次真正建立 Agent Loop 思维

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch4](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter4/%E7%AC%AC%E5%9B%9B%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E7%BB%8F%E5%85%B8%E8%8C%83%E5%BC%8F%E6%9E%84%E5%BB%BA.md)
- [OpenAI Agent Building Track](https://developers.openai.com/tracks/building-agents)

**今天学什么**

- 精读 Ch4 的 ReAct 部分：Reason/Act/Observe 的信息流。
- 区分内部推理、可执行 Action、环境 Observation。
- 理解 Observation 必须改变下一步决策，否则 Loop 没有意义。

**今天动手做什么**

- 不用 Agent 框架，写 mock ReAct loop。
- 工具：`search_section`、`get_paragraph`、`normalize_unit`。
- 保存每一步 event，而不是只打印最终答案。

**当天产出**

- `01-mini-agent-loop/react_loop_v0.py`

**验收测试 / 通过标准**

- [ ] 给定“抽取 28d 抗压强度”任务，必须出现至少一次 Tool → Observation → Next Decision。
- [ ] Trace 中每步有 `step/type/input/output/error`。

### Day 5 — Plan-and-Solve：什么时候应先规划，再执行

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch4](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter4/%E7%AC%AC%E5%9B%9B%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E7%BB%8F%E5%85%B8%E8%8C%83%E5%BC%8F%E6%9E%84%E5%BB%BA.md)
- [OpenAI Practical Guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)

**今天学什么**

- 精读 Plan-and-Solve 部分。
- 理解“一次性生成计划”与“逐步 ReAct”的差异。
- 识别长任务中的 plan drift、计划过细、计划失效。

**今天动手做什么**

- 实现 `planner.py`，输出结构化步骤列表。
- 实现最小 executor，逐步执行并记录 `planned_step_id`。
- 用“抽取配方 + 养护 + 3/7/28d 强度”做任务。

**当天产出**

- `01-mini-agent-loop/plan_solve_v0.py`

**验收测试 / 通过标准**

- [ ] 计划必须可机读且每步有完成状态。
- [ ] 中途注入“未找到养护温度”，系统必须标记 blocked/replan，而非伪造。

### Day 6 — Reflection：反思不是“再问一次模型”

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch4](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter4/%E7%AC%AC%E5%9B%9B%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E7%BB%8F%E5%85%B8%E8%8C%83%E5%BC%8F%E6%9E%84%E5%BB%BA.md)

**今天学什么**

- 精读 Reflection 部分。
- 掌握 Execute → Critique → Refine。
- 理解 Critic 的评价维度必须显式，否则只是昂贵重写。

**今天动手做什么**

- 实现 extractor → critic → revise。
- Critic 输出固定 schema：事实性、证据充分性、单位一致性、遗漏。
- 构造一个故意错误的 52.4 MPa→52.4 GPa 样例。

**当天产出**

- `01-mini-agent-loop/reflection_v0.py`

**验收测试 / 通过标准**

- [ ] Critic 必须定位单位错误并给出证据。
- [ ] 若初稿正确，Refine 不得无理由改值。

### Day 7 — Week 1 闭卷 Gate：用自己的语言重建经典范式

**时间预算：** 闭卷 60 min｜编码 70 min｜测试 30 min｜复盘 20 min（≈3 h）

**学习网站**

- [Hello-Agents Ch4](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter4/%E7%AC%AC%E5%9B%9B%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E7%BB%8F%E5%85%B8%E8%8C%83%E5%BC%8F%E6%9E%84%E5%BB%BA.md)

**今天学什么**

- 不新增内容，只复盘 Agent 边界、ReAct、Plan-and-Solve、Reflection。

**今天动手做什么**

- 关闭资料，画 4 张架构图。
- 从空文件重写 60–120 行最小 Agent Loop。
- 录制 8 分钟口述：为什么你的文献抽取不应一开始就多 Agent。

**当天产出**

- `reviews/week01-review.md` + `01-mini-agent-loop/closed_book_loop.py`

**验收测试 / 通过标准**

- [ ] 代码支持 tool call、observation、max_steps、final answer。
- [ ] 口述必须比较 3 种范式的适用条件。
- [ ] 任一项失败则 Week 1 不通过。

---

## Week 2 — 受控 Agent Loop 与代码兜底

### Day 8 — Tool Contract：工具是受约束接口，不是函数列表

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangChain Tools](https://docs.langchain.com/oss/python/langchain/tools)
- [Hello-Agents Ch4](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter4/%E7%AC%AC%E5%9B%9B%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E7%BB%8F%E5%85%B8%E8%8C%83%E5%BC%8F%E6%9E%84%E5%BB%BA.md)

**今天学什么**

- 学习 name、description、args schema、return schema、error semantics、side effects、idempotency。
- 理解工具描述会影响模型路由，但不能替代运行时校验。

**今天动手做什么**

- 为 5 个文献工具写 Tool Spec。
- 实现统一 `ToolResult(ok,data,error,retryable,latency_ms)`。

**当天产出**

- `01-mini-agent-loop/tools/` + `docs/tool-contracts.md`

**验收测试 / 通过标准**

- [ ] 每个工具至少 3 个失败测试。
- [ ] 副作用工具必须显式标注。
- [ ] 未知工具名不得直接 `getattr` 执行。

### Day 9 — Agent Loop 工程化：停止、预算、重复调用检测

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Agent Learning Hub](https://github.com/datawhalechina/Agent-Learning-Hub)
- [OpenAI Practical Guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)

**今天学什么**

- 理解 max_steps、timeout、token/cost budget、duplicate-call detection、circuit breaker。
- 把“结束”视为系统策略，而非模型自觉。

**今天动手做什么**

- 给 Loop 增加预算对象和重复调用哈希。
- 构造模型连续 4 次调用相同工具的故障。

**当天产出**

- `01-mini-agent-loop/runtime.py`

**验收测试 / 通过标准**

- [ ] 重复调用在阈值内被停止。
- [ ] 超时返回 typed error。
- [ ] 达到预算时保留 partial result，而非崩溃。

### Day 10 — 错误处理：Retry、Fallback、Escalation 不是一回事

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangChain Middleware](https://docs.langchain.com/oss/python/langchain/middleware/overview)
- [OpenAI Practical Guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)

**今天学什么**

- 区分 retryable / non-retryable。
- 区分同工具重试、换工具 fallback、请求人工 escalation。
- 理解指数退避思想，但今天不追求完整库。

**今天动手做什么**

- 实现错误分类器。
- 让 `search_section` 超时→重试；schema error→修复一次；权限错误→直接失败。

**当天产出**

- `01-mini-agent-loop/errors.py` + `tests/test_error_policy.py`

**验收测试 / 通过标准**

- [ ] 至少 6 类错误各有明确策略。
- [ ] 禁止所有异常统一 `except Exception: retry`。

### Day 11 — “概率性核心 + 确定性外壳”：代码兜底第一版

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch4](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter4/%E7%AC%AC%E5%9B%9B%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E7%BB%8F%E5%85%B8%E8%8C%83%E5%BC%8F%E6%9E%84%E5%BB%BA.md)
- [LangChain Structured Output](https://docs.langchain.com/oss/python/langchain/structured-output)

**今天学什么**

- 理解哪些任务适合 LLM：语义定位、歧义判断、证据解释。
- 哪些必须确定性：Schema、单位换算、范围、数据库约束。

**今天动手做什么**

- 实现 `DeterministicValidator`：MPa/GPa、百分比、龄期、数值范围。
- 把 LLM 抽取结果接到 validator。

**当天产出**

- `01-mini-agent-loop/validators.py`

**验收测试 / 通过标准**

- [ ] 故意输入 52.4 GPa 抗压强度时被告警。
- [ ] `w/b=-0.2`、`age=29d` 等异常被定位到字段级。

### Day 12 — 文献抽取 V0：第一次形成端到端 Agent

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch4](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter4/%E7%AC%AC%E5%9B%9B%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E7%BB%8F%E5%85%B8%E8%8C%83%E5%BC%8F%E6%9E%84%E5%BB%BA.md)

**今天学什么**

- 回顾经典范式，选择你的 V0：建议 ReAct + deterministic validation。

**今天动手做什么**

- 输入一段真实或手写论文文本。
- 完成 section search → evidence fetch → extract → validate → final JSON。
- 所有字段保留 evidence span。

**当天产出**

- `01-mini-agent-loop/paper_agent_v0.py`

**验收测试 / 通过标准**

- [ ] 单命令运行。
- [ ] 至少抽取 5 个字段。
- [ ] 每个非空字段必须有 evidence。
- [ ] Validator 失败时不得静默通过。

### Day 13 — 建立第一个 Eval Set：从现在起禁止只看 Demo

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangSmith Evaluation Concepts](https://docs.langchain.com/langsmith/evaluation-concepts)
- [Hello-Agents Ch12](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter12/%E7%AC%AC%E5%8D%81%E4%BA%8C%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E6%80%A7%E8%83%BD%E8%AF%84%E4%BC%B0.md)

**今天学什么**

- 快速理解 dataset / example / evaluator。
- 今天不学完整评估框架，只建立“固定题集”习惯。

**今天动手做什么**

- 制作 20 条 JSONL：正常、缺失、单位冲突、跨段落、诱导性文本。
- 定义 expected fields 和 expected evidence keywords。

**当天产出**

- `datasets/v0_eval_20.jsonl`

**验收测试 / 通过标准**

- [ ] 20 条数据能被脚本加载。
- [ ] 至少 30% 是失败/边界样例。
- [ ] 禁止全是自己最容易的样例。

### Day 14 — Level 0 验收：Agent 思维与无框架 Loop

**时间预算：** 闭卷 40 min｜运行评测 60 min｜故障分析 50 min｜口述 20 min（≈2 h 50 min）

**学习网站**

- [Hello-Agents Ch1](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter1/%E7%AC%AC%E4%B8%80%E7%AB%A0%20%E5%88%9D%E8%AF%86%E6%99%BA%E8%83%BD%E4%BD%93.md)
- [Hello-Agents Ch4](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter4/%E7%AC%AC%E5%9B%9B%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E7%BB%8F%E5%85%B8%E8%8C%83%E5%BC%8F%E6%9E%84%E5%BB%BA.md)

**今天学什么**

- 只验收，不新增知识。

**今天动手做什么**

- 闭卷解释 10 个核心概念。
- 跑 20 条 Eval。
- 对 3 个失败 case 写 root cause。
- 从空白图重画文献抽取 Agent V0 数据流。

**当天产出**

- `level-gates/level0.md`

**验收测试 / 通过标准**

- [ ] 20 条中 Schema valid rate=100%。
- [ ] Agent 无无限循环。
- [ ] 能解释 ReAct/Plan/Reflection 的选择边界。
- [ ] 能指出至少 3 个“此处不该用 LLM”的位置。

---

# Level 1 — 自研 Agent Harness + LangChain v1

**周期：** Week 3–4  
**Level 主要产出：** `自研 mini framework + single-agent extractor v1`  
**晋级本质：** 既能造轮子，又能解释现代 Agent harness 的抽象

## Week 3 — 从零构建 Agent Harness

### Day 15 — HelloAgents 框架总览：先读架构，再读代码

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch7](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter7/%E7%AC%AC%E4%B8%83%E7%AB%A0%20%E6%9E%84%E5%BB%BA%E4%BD%A0%E7%9A%84Agent%E6%A1%86%E6%9E%B6.md)

**今天学什么**

- 精读 Ch7 的设计目标、目录结构、核心抽象。
- 重点观察 Agent、LLM、Message、Tool、Registry 的依赖方向。
- 批判性理解“万物皆 Tool”：学习价值与工程局限。

**今天动手做什么**

- 画出 HelloAgents 依赖图。
- 写 ADR-001：为什么你的教学框架不直接复制 HelloAgents。

**当天产出**

- `02-agent-framework/docs/architecture.md` + `adr/001-framework-scope.md`

**验收测试 / 通过标准**

- [ ] 能解释 LLMClient 与 Agent 分离的原因。
- [ ] 能指出“Memory/RAG 都当 Tool”至少 2 个局限。

### Day 16 — Message 与 Event Model：先定义系统语言

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch7](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter7/%E7%AC%AC%E4%B8%83%E7%AB%A0%20%E6%9E%84%E5%BB%BA%E4%BD%A0%E7%9A%84Agent%E6%A1%86%E6%9E%B6.md)

**今天学什么**

- 学习 Message 抽象与消息角色。
- 额外区分 message 与 runtime event；不要把日志塞进 messages。

**今天动手做什么**

- 实现 `Message`、`ToolCall`、`ToolObservation`、`RunEvent`。
- 加入序列化/反序列化。

**当天产出**

- `02-agent-framework/core/message.py` + `core/events.py`

**验收测试 / 通过标准**

- [ ] round-trip serialization 测试通过。
- [ ] Event 可记录但不进入模型上下文。

### Day 17 — LLM Adapter：模型供应商不能污染 Agent 核心

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch7](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter7/%E7%AC%AC%E4%B8%83%E7%AB%A0%20%E6%9E%84%E5%BB%BA%E4%BD%A0%E7%9A%84Agent%E6%A1%86%E6%9E%B6.md)
- [LangChain Overview](https://docs.langchain.com/oss/python/langchain/overview)

**今天学什么**

- 理解 adapter/interface。
- 定义模型返回的统一 `ModelDecision`。

**今天动手做什么**

- 实现 `BaseLLM` protocol 和 `MockLLM`。
- 可选接一个真实 provider，但测试默认不能依赖 API。

**当天产出**

- `02-agent-framework/core/llm.py`

**验收测试 / 通过标准**

- [ ] MockLLM 能脚本化返回 tool call / final。
- [ ] Agent 测试无 API key 也能运行。

### Day 18 — Tool Registry 与安全执行边界

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch7](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter7/%E7%AC%AC%E4%B8%83%E7%AB%A0%20%E6%9E%84%E5%BB%BA%E4%BD%A0%E7%9A%84Agent%E6%A1%86%E6%9E%B6.md)
- [LangChain Tools](https://docs.langchain.com/oss/python/langchain/tools)

**今天学什么**

- 学习工具注册、schema 暴露、执行分离。
- 理解 registry 是 capability boundary。

**今天动手做什么**

- 实现装饰器或显式注册 API。
- 重复名称拒绝注册；参数校验；白名单执行。

**当天产出**

- `02-agent-framework/tools/registry.py` + `executor.py`

**验收测试 / 通过标准**

- [ ] 未知工具拒绝。
- [ ] 非法参数不进入函数体。
- [ ] 5 个工具可枚举出 schema。

### Day 19 — BaseAgent：把 Loop 从脚本升级成可复用 Harness

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch7](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter7/%E7%AC%AC%E4%B8%83%E7%AB%A0%20%E6%9E%84%E5%BB%BA%E4%BD%A0%E7%9A%84Agent%E6%A1%86%E6%9E%B6.md)

**今天学什么**

- 学习 BaseAgent 生命周期。
- 明确 runtime config、messages、tools、budget、events 的归属。

**今天动手做什么**

- 实现 `BaseAgent.run()` 和 hooks：before_model / after_model / before_tool / after_tool。

**当天产出**

- `02-agent-framework/agents/base.py`

**验收测试 / 通过标准**

- [ ] 最大步数生效。
- [ ] 任一步异常生成 event。
- [ ] 至少 4 个 hooks 可独立测试。

### Day 20 — 实现 ReActAgent，并与 Week 1 版本对照

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch7](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter7/%E7%AC%AC%E4%B8%83%E7%AB%A0%20%E6%9E%84%E5%BB%BA%E4%BD%A0%E7%9A%84Agent%E6%A1%86%E6%9E%B6.md)
- [Hello-Agents Ch4](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter4/%E7%AC%AC%E5%9B%9B%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E7%BB%8F%E5%85%B8%E8%8C%83%E5%BC%8F%E6%9E%84%E5%BB%BA.md)

**今天学什么**

- 比较教学脚本与框架抽象的差异。

**今天动手做什么**

- 基于 BaseAgent 实现 ReActAgent。
- 同一 20-case eval 同时跑旧版与新版。

**当天产出**

- `02-agent-framework/agents/react.py` + `reports/react_ablation.md`

**验收测试 / 通过标准**

- [ ] 功能不低于旧版。
- [ ] 新增框架没有改变 expected output schema。
- [ ] 报告中列出抽象收益和复杂度成本。

### Day 21 — Week 3 Gate：闭卷重建最小 Agent Harness

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch7](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter7/%E7%AC%AC%E4%B8%83%E7%AB%A0%20%E6%9E%84%E5%BB%BA%E4%BD%A0%E7%9A%84Agent%E6%A1%86%E6%9E%B6.md)

**今天学什么**

- 不新增知识。

**今天动手做什么**

- 从空目录重建最小 `Message → LLM → ToolRegistry → AgentLoop`。
- 只允许查看自己的接口文档，不看实现。

**当天产出**

- `reviews/week03-from-scratch/`

**验收测试 / 通过标准**

- [ ] ≤180 行核心代码跑通 5 case。
- [ ] 能口述 tool schema 如何从注册到执行。
- [ ] 能定位 stop condition 属于哪一层。

---

## Week 4 — LangChain v1 单 Agent 工程

### Day 22 — LangChain v1 心智模型：Agent = Model + Harness

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangChain Overview](https://docs.langchain.com/oss/python/langchain/overview)
- [LangChain Agents](https://docs.langchain.com/oss/python/langchain/agents)

**今天学什么**

- 只学当前 v1 抽象：model、tools、create_agent、middleware、state。
- 把官方抽象映射到你 Week 3 自己写的组件。

**今天动手做什么**

- 写“自研框架 ↔ LangChain v1”映射表。
- 跑最小 `create_agent` 示例。

**当天产出**

- `03-single-agent/langchain_mapping.md` + `hello_agent.py`

**验收测试 / 通过标准**

- [ ] 映射表至少 8 项。
- [ ] 能解释 LangChain 替你封装了哪些 Loop 逻辑。

### Day 23 — LangChain Tools：重构你的文献工具

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangChain Tools](https://docs.langchain.com/oss/python/langchain/tools)

**今天学什么**

- 学习 `@tool`、schema、ToolRuntime 的边界。
- 理解哪些参数对模型隐藏。

**今天动手做什么**

- 把 5 个 V0 工具迁移到 LangChain tools。
- 保留原确定性 validator。

**当天产出**

- `03-single-agent/tools.py`

**验收测试 / 通过标准**

- [ ] 工具 schema 可打印检查。
- [ ] runtime-only 参数不暴露给模型。
- [ ] 原工具单测继续通过。

### Day 24 — Structured Output：生产抽取不接受自由文本 JSON

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangChain Structured Output](https://docs.langchain.com/oss/python/langchain/structured-output)

**今天学什么**

- 学习 response_format 与结构化响应。
- 理解 provider-native 与 tool strategy 的概念差异。

**今天动手做什么**

- 创建 `PaperExtraction` schema。
- 输出 composition/properties/experiment/evidence/warnings。

**当天产出**

- `03-single-agent/schemas.py` + `extractor_v1.py`

**验收测试 / 通过标准**

- [ ] 20-case Schema valid rate=100%。
- [ ] 缺失字段用 `null + missing_reason`，禁止捏造。

### Day 25 — Short-term Memory 与 State：不要把一切塞进 messages

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangChain Short-term Memory](https://docs.langchain.com/oss/python/langchain/short-term-memory)

**今天学什么**

- 区分消息历史、运行状态、自定义 state 字段。
- 理解 thread-scoped state。

**今天动手做什么**

- 增加 `paper_id`、`retrieved_sections`、`validation_errors` 状态。
- 让工具可读取必要 state。

**当天产出**

- `03-single-agent/state.py`

**验收测试 / 通过标准**

- [ ] 两个 paper/thread 的状态不串。
- [ ] 工具只读取必要字段。

### Day 26 — Middleware：横切逻辑不应散落在 Prompt

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangChain Middleware](https://docs.langchain.com/oss/python/langchain/middleware/overview)
- [LangChain Context Engineering](https://docs.langchain.com/oss/python/langchain/context-engineering)

**今天学什么**

- 学习 hook/lifecycle 思维。
- 识别 logging、retry、early stop、context shaping。

**今天动手做什么**

- 实现至少 2 个 middleware：运行预算、模型调用日志。
- 可选：高风险工具拦截。

**当天产出**

- `03-single-agent/middleware.py`

**验收测试 / 通过标准**

- [ ] middleware 可单独禁用。
- [ ] 禁用后核心 Agent 不改代码。
- [ ] Budget 超限有明确终止原因。

### Day 27 — 单 Agent Paper Extractor v1：形成第一个可投作品雏形

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangChain Agents](https://docs.langchain.com/oss/python/langchain/agents)
- [LangChain RAG](https://docs.langchain.com/oss/python/langchain/rag)

**今天学什么**

- 理解 agentic retrieval 与固定 retrieval workflow 的差别。

**今天动手做什么**

- 完成 `paper-extractor-agent-v1`：检索段落→抽取→验证→输出。
- 加入 CLI。

**当天产出**

- `03-single-agent/` 完整可运行目录

**验收测试 / 通过标准**

- [ ] `python -m ... --input sample.txt` 可运行。
- [ ] 20-case eval 有指标报告。
- [ ] README 包含架构图、限制和失败案例。

### Day 28 — Level 1 验收：会造轮子，也会用现代 Harness

**时间预算：** 闭卷 40 min｜A/B 评测 80 min｜Trace 分析 40 min｜总结 15 min（≈2 h 55 min）

**学习网站**

- [Hello-Agents Ch7](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter7/%E7%AC%AC%E4%B8%83%E7%AB%A0%20%E6%9E%84%E5%BB%BA%E4%BD%A0%E7%9A%84Agent%E6%A1%86%E6%9E%B6.md)
- [LangChain Agents](https://docs.langchain.com/oss/python/langchain/agents)

**今天学什么**

- 只验收。

**今天动手做什么**

- 闭卷比较自研 Harness 与 LangChain v1。
- 对 20-case 运行自研 ReAct、LangChain Agent 两组实验。
- 解释 3 个失败 trace。

**当天产出**

- `level-gates/level1.md`

**验收测试 / 通过标准**

- [ ] 能从模型 decision 追到 tool execution。
- [ ] 结构化输出 100% 可解析。
- [ ] 无框架与框架版都能运行。
- [ ] 能说明何时不该继续维护自研框架。

---

# Level 2 — LangGraph 状态化编排 + Persistence + HITL

**周期：** Week 5–6  
**Level 主要产出：** `paper-extraction-graph-v2`  
**晋级本质：** 能构建可暂停、可恢复、可测试的 stateful agent

## Week 5 — LangGraph StateGraph 与显式控制流

### Day 29 — 为什么需要 LangGraph：从 Agent Loop 转向显式状态机

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview)
- [Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph)

**今天学什么**

- 理解 long-running、stateful、durable execution、HITL 的需求。
- 区分高层 agent harness 与低层 orchestration runtime。

**今天动手做什么**

- 把 v1 extractor 的隐式流程画成 StateGraph。
- 标出 deterministic nodes 与 agentic nodes。

**当天产出**

- `04-langgraph-extractor/design_v2.md`

**验收测试 / 通过标准**

- [ ] 至少 6 个 node。
- [ ] 每个 node 有单一职责。
- [ ] 能解释为什么某一步不应是 Agent node。

### Day 30 — State Schema：先设计状态，再写 Node

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph)
- [LangGraph Workflows + Agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents)

**今天学什么**

- 理解 state 是节点之间的契约。
- 区分输入字段、中间字段、输出字段、审计字段。

**今天动手做什么**

- 定义 `ExtractionState`。
- 包含 paper_id、goal、evidence、draft、validation、retry_count、status。

**当天产出**

- `04-langgraph-extractor/state.py`

**验收测试 / 通过标准**

- [ ] 字段拥有明确 owner。
- [ ] 禁止一个 `misc: dict` 承担所有内容。
- [ ] 能解释 reducer/merge 冲突风险。

### Day 31 — Node 设计：把节点做成可测函数

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangGraph Workflows + Agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents)

**今天学什么**

- 学习 node 的输入输出边界。
- 优先纯函数与依赖注入。

**今天动手做什么**

- 实现 retrieve / extract / validate 三节点。
- 模型调用封装为依赖。

**当天产出**

- `04-langgraph-extractor/nodes.py`

**验收测试 / 通过标准**

- [ ] 3 个节点可独立单测。
- [ ] Validator node 不调用 LLM。
- [ ] 节点不直接修改全局变量。

### Day 32 — Conditional Edge：把失败策略显式化

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangGraph Workflows + Agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents)

**今天学什么**

- 学习 routing function。
- 理解 route 结果必须有限、可测。

**今天动手做什么**

- 实现 `route_after_validation`：accept / retry_extract / retrieve_more / human_review。

**当天产出**

- `04-langgraph-extractor/routing.py`

**验收测试 / 通过标准**

- [ ] 至少 8 个参数化路由测试。
- [ ] 相同 state 输入路由结果确定。

### Day 33 — Loop 与终止：图也会死循环

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangGraph Workflows + Agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
- [Agent Learning Hub](https://github.com/datawhalechina/Agent-Learning-Hub)

**今天学什么**

- 理解图循环、retry counter、repeated state detection。

**今天动手做什么**

- 增加 retry budget、same-error fingerprint。
- 故障注入：evidence 永远缺失。

**当天产出**

- `04-langgraph-extractor/guards.py`

**验收测试 / 通过标准**

- [ ] 最多 N 次后停止。
- [ ] 停止时返回 failure taxonomy，不只 `failed`。

### Day 34 — LangGraph 101：运行官方课程，不只看文档

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangGraph 101](https://github.com/langchain-ai/langgraph-101)

**今天学什么**

- 运行 101 Fundamentals 中与你当前能力对应的 notebook。
- 重点比较 StateGraph、tools、memory、streaming。

**今天动手做什么**

- 至少改一个 notebook：替换成材料文献工具。
- 记录 5 个“与我原理解不同”的点。

**当天产出**

- `00-notes/day34-langgraph101.md` + 修改后的 notebook

**验收测试 / 通过标准**

- [ ] Notebook 从头可运行。
- [ ] 至少一次主动修改而非原样执行。

### Day 35 — Week 5 Gate：闭卷搭出可路由 Extraction Graph

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview)

**今天学什么**

- 不新增知识。

**今天动手做什么**

- 从空文件创建 START→retrieve→extract→validate→conditional route→END。
- 用 MockLLM 跑 6 个 case。

**当天产出**

- `reviews/week05-graph-from-scratch.py`

**验收测试 / 通过标准**

- [ ] 6 case 覆盖 accept/retry/human。
- [ ] 能画出状态转移。
- [ ] 不能靠 prompt 文本模拟路由。

---

## Week 6 — Persistence、Memory、HITL 与恢复

### Day 36 — Persistence / Checkpointer：状态恢复是运行时能力

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangGraph Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)

**今天学什么**

- 精读 checkpoints、threads、state snapshots。
- 理解 persistence 与数据库业务存储不同。

**今天动手做什么**

- 给 graph 接入 checkpointer。
- 同一 thread 连续运行并读取 state history。

**当天产出**

- `04-langgraph-extractor/persistence_demo.py`

**验收测试 / 通过标准**

- [ ] 不同 thread 隔离。
- [ ] 可展示至少 3 个 checkpoint。

### Day 37 — Memory：短期状态、长期记忆、检索库三分法

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch8](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter8/%E7%AC%AC%E5%85%AB%E7%AB%A0%20%E8%AE%B0%E5%BF%86%E4%B8%8E%E6%A3%80%E7%B4%A2.md)
- [LangGraph Memory](https://docs.langchain.com/oss/python/langgraph/memory)
- [LangChain Long-term Memory](https://docs.langchain.com/oss/python/langchain/long-term-memory)

**今天学什么**

- 选择性阅读 Ch8：Memory/RAG/存储；重点建立分类。
- 区分 checkpoint state、store memory、vector retrieval。

**今天动手做什么**

- 写 `memory_decision_table.md`。
- 为文献抽取系统定义：论文级 state、用户偏好 memory、文献知识库。

**当天产出**

- `04-langgraph-extractor/memory_decision_table.md`

**验收测试 / 通过标准**

- [ ] 对 10 个信息项正确归类。
- [ ] 能解释“把所有历史全文放 messages”为什么错误。

### Day 38 — Interrupt：把“不确定”升级成可暂停状态

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangGraph Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)

**今天学什么**

- 理解 pause/resume、JSON-serializable payload、thread identity。

**今天动手做什么**

- 当 validation severity=high 时 `interrupt()`。
- payload 包含字段、候选值、证据、原因。

**当天产出**

- `04-langgraph-extractor/hitl.py`

**验收测试 / 通过标准**

- [ ] 运行到人工点确实暂停。
- [ ] 重启进程后在支持的持久化环境中可恢复，或至少用测试验证 resume。

### Day 39 — HITL Policy：不是所有低置信度都找人

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangGraph Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)

**今天学什么**

- 设计风险分级：auto-accept / auto-retry / human-review / reject。

**今天动手做什么**

- 为文献抽取系统写 12 条 policy。
- 示例：单位冲突、证据缺失、数据库写入、重复样品 ID。

**当天产出**

- `04-langgraph-extractor/hitl_policy.md`

**验收测试 / 通过标准**

- [ ] 每条 policy 有触发条件和行动。
- [ ] 能说明成本与风险权衡。

### Day 40 — Subgraph：为未来多 Agent 做边界准备

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangGraph Subgraphs](https://docs.langchain.com/oss/python/langgraph/use-subgraphs)

**今天学什么**

- 学习 subgraph 适用场景：复用、团队分工、状态隔离。

**今天动手做什么**

- 把 validation pipeline 封装为 subgraph。

**当天产出**

- `04-langgraph-extractor/subgraphs/validation_graph.py`

**验收测试 / 通过标准**

- [ ] 主图只依赖清晰输入输出。
- [ ] subgraph 单独可测。

### Day 41 — Paper Extraction Graph v2：持久化 + HITL 完整集成

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview)
- [Hello-Agents Ch8](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter8/%E7%AC%AC%E5%85%AB%E7%AB%A0%20%E8%AE%B0%E5%BF%86%E4%B8%8E%E6%A3%80%E7%B4%A2.md)

**今天学什么**

- 整合本周能力。

**今天动手做什么**

- 完成 graph v2。
- 加入 CLI：start/resume/status。
- 将 20-case eval 扩到 30 case。

**当天产出**

- `04-langgraph-extractor/` 完整项目

**验收测试 / 通过标准**

- [ ] 模拟中断后可恢复。
- [ ] 30 case 无无限循环。
- [ ] 每个 run 有 thread_id 和终止原因。

### Day 42 — Level 2 验收：Stateful Agent 工程能力

**时间预算：** 口述 35 min｜恢复演示 55 min｜测试 55 min｜总结 20 min（≈2 h 45 min）

**学习网站**

- [LangGraph Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [LangGraph Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)

**今天学什么**

- 只验收。

**今天动手做什么**

- 闭卷解释 State/Context/Memory/Persistence。
- 现场演示：启动→失败→checkpoint→人工输入→resume。
- 对 graph 做 10 个单元/路由测试。

**当天产出**

- `level-gates/level2.md`

**验收测试 / 通过标准**

- [ ] 能恢复，不从头重跑。
- [ ] HITL payload 可审计。
- [ ] 路由测试通过率 100%。
- [ ] 能解释 checkpointer 与业务数据库差异。

---

# Level 3 — Multi-Agent 协调 + DeepResearch 思维

**周期：** Week 7–8  
**Level 主要产出：** `paper-multi-agent-v3 + baseline study`  
**晋级本质：** 能证明何时多 Agent 有价值，何时没有

## Week 7 — Multi-Agent 模式与协调边界

### Day 43 — Multi-Agent 的第一原则：协调成本必须有收益

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangChain Multi-Agent](https://docs.langchain.com/oss/python/langchain/multi-agent)
- [Agent Learning Hub](https://github.com/datawhalechina/Agent-Learning-Hub)

**今天学什么**

- 学习 subagents、handoffs、router、custom workflow 等模式。
- 明确多 Agent 价值：context isolation、parallelism、specialization、permissions。

**今天动手做什么**

- 列出文献抽取系统拆成 5 Agent 的收益假设和反例。
- 定义 single-agent baseline。

**当天产出**

- `05-multi-agent/adr/002-why-multi-agent.md`

**验收测试 / 通过标准**

- [ ] 至少提出 3 个可测收益。
- [ ] 若收益无法测量，默认不拆。

### Day 44 — Router：显式分类与并行分发

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangChain Router](https://docs.langchain.com/oss/python/langchain/multi-agent/router)
- [Router Knowledge Base Tutorial](https://docs.langchain.com/oss/python/langchain/multi-agent/router-knowledge-base)

**今天学什么**

- 理解 router 适用于显式预处理、并行控制。

**今天动手做什么**

- 实现 document request router：composition/property/experiment/mixed。
- mixed 允许并行。

**当天产出**

- `05-multi-agent/router.py`

**验收测试 / 通过标准**

- [ ] 20 条路由集 accuracy≥90%。
- [ ] 路由输出 schema 固定。

### Day 45 — Subagents / Supervisor：中央协调何时合理

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangChain Subagents](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents)

**今天学什么**

- 学习主 Agent 将 subagent 作为工具调用的模式。
- 理解 centralized context 的优缺点。

**今天动手做什么**

- 实现 Composition、Property 两个 subagent。
- Supervisor 只接收压缩结果，不转发全文。

**当天产出**

- `05-multi-agent/subagents_v0.py`

**验收测试 / 通过标准**

- [ ] 两个 Agent 职责无重叠或能明确解释重叠。
- [ ] subagent 输出带 evidence。

### Day 46 — Handoff：控制权转移与 Agent-as-Tool 的区别

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangChain Handoffs](https://docs.langchain.com/oss/python/langchain/multi-agent/handoffs)
- [OpenAI Agents SDK Handoffs](https://openai.github.io/openai-agents-python/handoffs/)

**今天学什么**

- 比较 delegation as tool 与 handoff takeover。
- 理解 handoff 会改变谁拥有后续上下文/控制权。

**今天动手做什么**

- 用一个最小客服示例或文献例子分别实现两种模式。
- 写对照表。

**当天产出**

- `05-multi-agent/handoff_vs_tool.md` + demo

**验收测试 / 通过标准**

- [ ] 能指出文献抽取主链中哪些位置不适合 handoff。
- [ ] 两种实现 trace 可区分。

### Day 47 — Extractor–Verifier：你的核心多 Agent 模式

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch4](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter4/%E7%AC%AC%E5%9B%9B%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E7%BB%8F%E5%85%B8%E8%8C%83%E5%BC%8F%E6%9E%84%E5%BB%BA.md)
- [LangChain Multi-Agent](https://docs.langchain.com/oss/python/langchain/multi-agent)

**今天学什么**

- 把 Reflection 思想升级为职责隔离。
- Verifier 不应直接重写原结果。

**今天动手做什么**

- 实现 extractor → verifier → targeted repair。
- Verifier 输出 issue list 与 severity。

**当天产出**

- `05-multi-agent/extractor_verifier.py`

**验收测试 / 通过标准**

- [ ] Verifier 至少发现 3 类注入错误。
- [ ] repair 只修改被标记字段。

### Day 48 — 共享状态污染：多 Agent 最常见隐性故障

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangChain Context Engineering](https://docs.langchain.com/oss/python/langchain/context-engineering)
- [LangGraph Subgraphs](https://docs.langchain.com/oss/python/langgraph/use-subgraphs)

**今天学什么**

- 理解 context leakage、shared scratchpad、authority confusion。

**今天动手做什么**

- 给每个 Agent 定义最小输入 schema。
- 禁止 Composition Agent 看到无关长上下文。
- 记录 context bytes/tokens 近似量。

**当天产出**

- `05-multi-agent/context_contracts.md`

**验收测试 / 通过标准**

- [ ] 每个 Agent 的输入字段可列举。
- [ ] 至少减少一次无关上下文注入。

### Day 49 — Week 7 架构评审：用 ADR 而不是“感觉更高级”

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch13](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter13/%E7%AC%AC%E5%8D%81%E4%B8%89%E7%AB%A0%20%E6%99%BA%E8%83%BD%E6%97%85%E8%A1%8C%E5%8A%A9%E6%89%8B.md)
- [LangChain Multi-Agent](https://docs.langchain.com/oss/python/langchain/multi-agent)

**今天学什么**

- 选择性阅读 Ch13 的多 Agent 协作设计，不复制旅游业务。

**今天动手做什么**

- 做 30 分钟架构评审：Router vs Supervisor vs Custom Workflow。
- 产出最终 V3 拓扑。

**当天产出**

- `05-multi-agent/architecture_v3.md`

**验收测试 / 通过标准**

- [ ] 每条 Agent 边有 input/output/owner/stop condition。
- [ ] 能说明至少 2 个地方坚持用 deterministic workflow。

---

## Week 8 — DeepResearch 思维与多 Agent 文献抽取

### Day 50 — DeepResearch Agent：学习长任务分解，不照抄产品

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch14](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter14/%E7%AC%AC%E5%8D%81%E5%9B%9B%E7%AB%A0%20%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B7%B1%E5%BA%A6%E7%A0%94%E7%A9%B6%E6%99%BA%E8%83%BD%E4%BD%93.md)

**今天学什么**

- 精读：任务拆解、检索、迭代研究、综合。
- 关注长任务中的 query refinement、evidence accumulation。

**今天动手做什么**

- 把 DeepResearch 模式映射到“跨段落/跨表格文献抽取”。

**当天产出**

- `00-notes/day50-deepresearch-mapping.md`

**验收测试 / 通过标准**

- [ ] 至少识别 4 个可迁移设计。
- [ ] 至少指出 3 个不适用于单篇抽取的设计。

### Day 51 — Parallel Workers：能并行不代表应该并行

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Router Knowledge Base Tutorial](https://docs.langchain.com/oss/python/langchain/multi-agent/router-knowledge-base)
- [LangChain Custom Workflow](https://docs.langchain.com/oss/python/langchain/multi-agent/custom-workflow)

**今天学什么**

- 理解 Send/并行任务思想、汇总与冲突。

**今天动手做什么**

- 并行运行 composition/property/experiment workers。
- 记录 wall time 与总模型调用数。

**当天产出**

- `05-multi-agent/parallel_workers.py`

**验收测试 / 通过标准**

- [ ] 结果顺序不影响 merge。
- [ ] 单 worker 失败不吞掉其他结果。

### Day 52 — Evidence Merger：多 Agent 最终必须解决冲突

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch14](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter14/%E7%AC%AC%E5%8D%81%E5%9B%9B%E7%AB%A0%20%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B7%B1%E5%BA%A6%E7%A0%94%E7%A9%B6%E6%99%BA%E8%83%BD%E4%BD%93.md)

**今天学什么**

- 理解 synthesis 不是简单 concat。
- 设计 provenance-aware merge。

**今天动手做什么**

- 同一字段多个候选值时按 evidence、sample_id、condition 合并。

**当天产出**

- `05-multi-agent/merger.py`

**验收测试 / 通过标准**

- [ ] 冲突值不得静默覆盖。
- [ ] 输出保留来源 Agent 和 evidence id。

### Day 53 — 多 Agent Stop Condition 与反复争论检测

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Agent Learning Hub](https://github.com/datawhalechina/Agent-Learning-Hub)
- [LangChain Multi-Agent](https://docs.langchain.com/oss/python/langchain/multi-agent)

**今天学什么**

- 理解 ping-pong、critic loops、task drift。

**今天动手做什么**

- 增加 per-agent step budget、global budget、same-issue fingerprint。

**当天产出**

- `05-multi-agent/coordination_guards.py`

**验收测试 / 通过标准**

- [ ] 构造 Extractor↔Verifier 循环，系统在阈值内停止。
- [ ] partial results 可返回。

### Day 54 — 完成 paper-multi-agent-v3

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch16](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter16/%E7%AC%AC%E5%8D%81%E5%85%AD%E7%AB%A0%20%E6%AF%95%E4%B8%9A%E8%AE%BE%E8%AE%A1.md)
- [LangChain Subagents](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents)

**今天学什么**

- 选择性阅读 Ch16 的毕业设计要求，用作完整项目检查表。

**今天动手做什么**

- 集成 Router/Supervisor、3 专业 Agent、Verifier、Code Validator。
- 扩展 eval 到 50 case。

**当天产出**

- `05-multi-agent/` 可运行 V3

**验收测试 / 通过标准**

- [ ] 50 case 可批量运行。
- [ ] 每个 run 记录 Agent 路径。
- [ ] 所有字段含 provenance。

### Day 55 — Single vs Multi：第一次做真正架构实验

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangSmith Evaluation](https://docs.langchain.com/langsmith/evaluation)
- [LangChain Multi-Agent](https://docs.langchain.com/oss/python/langchain/multi-agent)

**今天学什么**

- 定义比较指标：field accuracy、evidence precision、latency、calls、cost proxy、failure rate。

**今天动手做什么**

- 同一 50-case 跑 v1 single 与 v3 multi。
- 固定模型/温度/数据。

**当天产出**

- `reports/single_vs_multi_v1.md` + CSV

**验收测试 / 通过标准**

- [ ] 报告必须允许得出“Multi-Agent 不更好”。
- [ ] 至少 5 个 case 做配对分析。

### Day 56 — Level 3 验收：Multi-Agent 是架构能力，不是角色扮演

**时间预算：** 口述 40 min｜三类演示 70 min｜实验答辩 45 min｜总结 15 min（≈2 h 50 min）

**学习网站**

- [Hello-Agents Ch13](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter13/%E7%AC%AC%E5%8D%81%E4%B8%89%E7%AB%A0%20%E6%99%BA%E8%83%BD%E6%97%85%E8%A1%8C%E5%8A%A9%E6%89%8B.md)
- [LangChain Multi-Agent](https://docs.langchain.com/oss/python/langchain/multi-agent)

**今天学什么**

- 只验收。

**今天动手做什么**

- 现场解释 Router/Subagents/Handoff/Custom Workflow。
- 演示一个并行 case、一个冲突 case、一个循环 case。
- 答辩 Single vs Multi 实验。

**当天产出**

- `level-gates/level3.md`

**验收测试 / 通过标准**

- [ ] 能说明每个 Agent 的必要性。
- [ ] 冲突不丢 provenance。
- [ ] 循环可停止。
- [ ] 有量化 baseline 对照。

---

# Level 4 — Evaluation + Tracing + Context Engineering + MCP

**周期：** Week 9–10  
**Level 主要产出：** `eval suite + context ablation + MCP server`  
**晋级本质：** 能用数据和 trace 驱动可靠性改进

## Week 9 — Agent Evaluation、Trajectory 与 Tracing

### Day 57 — Agent Evaluation 全景：最终答案只是一个层面

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch12](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter12/%E7%AC%AC%E5%8D%81%E4%BA%8C%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E6%80%A7%E8%83%BD%E8%AF%84%E4%BC%B0.md)
- [LangSmith Evaluation](https://docs.langchain.com/langsmith/evaluation)

**今天学什么**

- 精读 Ch12 中指标/benchmark/evaluation framework。
- 学习 offline eval、online eval、dataset、evaluator、experiment。

**今天动手做什么**

- 写 Literature Extraction Eval Spec v1。
- 分 response / field / evidence / tool / trajectory / system。

**当天产出**

- `06-evaluation/eval_spec.md`

**验收测试 / 通过标准**

- [ ] 每个指标有定义、输入、计算方法、阈值。
- [ ] 禁止“效果不错”这类不可测标准。

### Day 58 — 正式 Eval Dataset：从 50 条扩到 ≥80 条

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangSmith Evaluation Concepts](https://docs.langchain.com/langsmith/evaluation-concepts)

**今天学什么**

- 学习 curated cases、production traces、synthetic cases 的角色。

**今天动手做什么**

- 扩到至少 80 条，推荐 100。
- 按 normal/missing/conflict/cross-section/table-like/adversarial 分层。

**当天产出**

- `datasets/literature_eval_v1.jsonl` + dataset card

**验收测试 / 通过标准**

- [ ] ≥80 条。
- [ ] 每类有最少样本。
- [ ] 人工检查随机 15 条 gold。

### Day 59 — Deterministic Evaluators：能用代码判断就别先用 Judge

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangSmith Evaluation](https://docs.langchain.com/langsmith/evaluation)

**今天学什么**

- 学习 code evaluators。

**今天动手做什么**

- 实现 schema validity、exact/normalized match、unit validity、evidence substring、tool whitelist。

**当天产出**

- `06-evaluation/evaluators/deterministic.py`

**验收测试 / 通过标准**

- [ ] 至少 5 个 evaluator。
- [ ] 每个有独立单测。

### Day 60 — LLM-as-Judge：只评代码难以定义的质量

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangSmith Evaluation](https://docs.langchain.com/langsmith/evaluation)
- [Hello-Agents Ch12](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter12/%E7%AC%AC%E5%8D%81%E4%BA%8C%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E6%80%A7%E8%83%BD%E8%AF%84%E4%BC%B0.md)

**今天学什么**

- 学习 rubric、reference-based vs reference-free、judge bias。

**今天动手做什么**

- 设计 evidence sufficiency 与 explanation quality rubric。
- 抽 20 条做双重评审。

**当天产出**

- `06-evaluation/evaluators/judge.py` + `judge_rubric.md`

**验收测试 / 通过标准**

- [ ] Rubric 有 1–5 级锚点。
- [ ] 同样输入重复评审差异被记录。

### Day 61 — Trajectory Evaluation：评工具顺序和路径

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangSmith Trajectory Evals](https://docs.langchain.com/langsmith/trajectory-evals)
- [Evaluate Complex Agent](https://docs.langchain.com/langsmith/evaluate-complex-agent)

**今天学什么**

- 理解 exact match、subset/subsequence、LLM judge。

**今天动手做什么**

- 为 20 条关键 case 定 expected trajectory。
- 评估是否先检索证据再抽取。

**当天产出**

- `06-evaluation/trajectory_eval.py`

**验收测试 / 通过标准**

- [ ] 能识别“答案对但先猜后补证据”的坏轨迹。
- [ ] 输出轨迹失败原因。

### Day 62 — Tracing：从失败结果回到失败步骤

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [OpenAI Agents SDK Tracing](https://openai.github.io/openai-agents-python/tracing/)
- [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview)

**今天学什么**

- 理解 trace/span/event。
- 选择 LangSmith 或自研结构化 trace；可横向看 OpenAI SDK。

**今天动手做什么**

- 对 10 个失败 run 做 trace review。
- 标注 failure stage。

**当天产出**

- `reports/trace_failure_review.md`

**验收测试 / 通过标准**

- [ ] 至少分 prompt/tool/retrieval/model/state/routing 6 类。
- [ ] 每类给一个修复策略。

### Day 63 — Week 9 Eval Gate：建立回归基线

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangSmith Evaluate Graph](https://docs.langchain.com/langsmith/evaluate-graph)

**今天学什么**

- 不新增内容。

**今天动手做什么**

- 跑 ≥80 case 的 v1/v3。
- 生成机器可读 metrics.json 和人读 report。
- 固定随机性设置与版本信息。

**当天产出**

- `06-evaluation/baseline/`

**验收测试 / 通过标准**

- [ ] 报告包含置信区间或至少样本数。
- [ ] 任何后续改动都能重跑。
- [ ] 失败分类覆盖≥90%失败 case。

---

## Week 10 — Context Engineering 与 MCP

### Day 64 — Context Engineering：决定模型这一刻看到什么

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch9](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter9/%E7%AC%AC%E4%B9%9D%E7%AB%A0%20%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B.md)
- [LangChain Context Engineering](https://docs.langchain.com/oss/python/langchain/context-engineering)

**今天学什么**

- 精读 Ch9 核心；对照官方 context engineering。
- 区分 model context、tool context、lifecycle context。

**今天动手做什么**

- 为文献抽取系统画 Context Map：每个 Agent 看什么、不看什么。

**当天产出**

- `07-context-mcp/context_map.md`

**验收测试 / 通过标准**

- [ ] 每类上下文有 owner、生命周期、裁剪策略。
- [ ] 能指出 3 个当前 context pollution。

### Day 65 — Context Budget：压缩、选择、摘要必须可测

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch9](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter9/%E7%AC%AC%E4%B9%9D%E7%AB%A0%20%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B.md)
- [LangChain Context Engineering](https://docs.langchain.com/oss/python/langchain/context-engineering)

**今天学什么**

- 学习 selection、compression、summarization、offloading 思路。

**今天动手做什么**

- 实现 evidence windowing。
- 比较 full-text vs top-k evidence context。

**当天产出**

- `07-context-mcp/context_ablation.py`

**验收测试 / 通过标准**

- [ ] 记录质量、输入长度 proxy、延迟。
- [ ] 若压缩损失质量，报告必须承认。

### Day 66 — Memory 与 Retrieval 再定位：不是所有知识都进 Prompt

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch8](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter8/%E7%AC%AC%E5%85%AB%E7%AB%A0%20%E8%AE%B0%E5%BF%86%E4%B8%8E%E6%A3%80%E7%B4%A2.md)
- [LangChain RAG](https://docs.langchain.com/oss/python/langchain/rag)

**今天学什么**

- 回顾 memory/RAG 与 context 的关系。

**今天动手做什么**

- 为“论文全文、用户字段模板、历史修正、单位规则”选择存储与注入策略。

**当天产出**

- `07-context-mcp/storage_context_decisions.md`

**验收测试 / 通过标准**

- [ ] 四类信息各有读取时机。
- [ ] 长期记忆不自动等于向量库。

### Day 67 — MCP：协议层，不是新 Agent 框架

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch10](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter10/%E7%AC%AC%E5%8D%81%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE.md)
- [MCP Intro](https://modelcontextprotocol.io/docs/getting-started/intro)
- [MCP Architecture](https://modelcontextprotocol.io/docs/learn/architecture)

**今天学什么**

- 精读 Ch10 中 MCP；对照官方定义。
- 理解 host/client/server、tools/resources/prompts。
- A2A/ANP 只了解，不投入实现。

**今天动手做什么**

- 画 MCP 架构图。
- 列出文献抽取系统中哪些能力值得 MCP 化。

**当天产出**

- `07-context-mcp/mcp_design.md`

**验收测试 / 通过标准**

- [ ] 能口述 MCP 与 Tool、Skill、Agent 的区别。
- [ ] 禁止把“用了 MCP”当成“多 Agent”。

### Day 68 — 构建第一个 MCP Server

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [MCP Build Server](https://modelcontextprotocol.io/docs/develop/build-server)
- [MCP Python SDK](https://py.sdk.modelcontextprotocol.io/)

**今天学什么**

- 按官方 Python 路线实现 server。

**今天动手做什么**

- 暴露 2–3 个只读工具：search_section、get_evidence、normalize_unit。

**当天产出**

- `07-context-mcp/literature_mcp_server/`

**验收测试 / 通过标准**

- [ ] server 能启动。
- [ ] 输入 schema 有效。
- [ ] 非法参数返回明确错误。

### Day 69 — MCP 接入 Agent：验证“解耦”是否真的发生

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [MCP Examples](https://modelcontextprotocol.io/examples)
- [MCP Intro](https://modelcontextprotocol.io/docs/getting-started/intro)

**今天学什么**

- 理解 server 可被不同 client 复用。

**今天动手做什么**

- 让一个 Agent client 调用文献抽取 MCP Server。
- 保留原 in-process tool 作为 baseline。

**当天产出**

- `07-context-mcp/mcp_client_demo.py`

**验收测试 / 通过标准**

- [ ] 相同 10 case 结果语义一致。
- [ ] 记录额外 latency。
- [ ] server 挂掉时有降级/错误。

### Day 70 — Level 4 验收：Eval + Context + MCP

**时间预算：** 回归评测 60 min｜演示 50 min｜Trace 答辩 45 min｜总结 15 min（≈2 h 50 min）

**学习网站**

- [Hello-Agents Ch12](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter12/%E7%AC%AC%E5%8D%81%E4%BA%8C%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E6%80%A7%E8%83%BD%E8%AF%84%E4%BC%B0.md)
- [MCP Intro](https://modelcontextprotocol.io/docs/getting-started/intro)

**今天学什么**

- 只验收。

**今天动手做什么**

- 演示 ≥80-case regression。
- 解释 3 个 trace failure。
- 演示 context ablation。
- 演示 MCP server/client。

**当天产出**

- `level-gates/level4.md`

**验收测试 / 通过标准**

- [ ] 有 deterministic + judge + trajectory eval。
- [ ] MCP 不是伪封装。
- [ ] 能用数据说明 context 策略收益/代价。
- [ ] 有回归阈值。

---

# Level 5 — Production + Portfolio + Interview

**周期：** Week 11–12  
**Level 主要产出：** `Multi-Agent Literature Extraction System`  
**晋级本质：** 达到可 clone、可运行、可评估、可答辩的求职作品水平

## Week 11 — Production API、测试与 Docker

### Day 71 — 生产项目重构：从 notebook 集合变成软件包

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Agent Learning Hub](https://github.com/datawhalechina/Agent-Learning-Hub)

**今天学什么**

- 学习应用边界：domain、agents、tools、runtime、api、tests。

**今天动手做什么**

- 重构 Multi-Agent Literature Extraction System 目录。
- 移除 notebook-only 依赖路径。

**当天产出**

- `08-production-app/`

**验收测试 / 通过标准**

- [ ] 全新 clone 环境可安装。
- [ ] 核心模块无循环 import。
- [ ] 配置不硬编码 key。

### Day 72 — FastAPI Contract：Agent 运行必须有稳定 API

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)

**今天学什么**

- 学习 request/response models、status code、dependency basics。

**今天动手做什么**

- 实现 POST `/runs`、GET `/runs/{id}`、POST `/runs/{id}/resume`。

**当天产出**

- `08-production-app/api/`

**验收测试 / 通过标准**

- [ ] OpenAPI 自动生成。
- [ ] 非法请求 4xx，不是 500。
- [ ] response schema 固定。

### Day 73 — Async 与并发：I/O 并发不是多线程魔法

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [FastAPI Async](https://fastapi.tiangolo.com/async/)

**今天学什么**

- 理解 await、I/O-bound、blocking call。

**今天动手做什么**

- 并发 3 个 independent worker。
- 对同步/异步做小 benchmark。

**当天产出**

- `08-production-app/benchmarks/async_bench.py`

**验收测试 / 通过标准**

- [ ] 无 event loop blocking 的明显长同步调用。
- [ ] benchmark 有任务规模说明。

### Day 74 — Testing：Agent 测试必须大量 Mock 与参数化

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [pytest Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [pytest Parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html)

**今天学什么**

- 学习 unit/integration/e2e 分层。
- 理解 MockLLM、fake tool、golden dataset。

**今天动手做什么**

- 补齐 node/tool/router/api 测试。
- 使用参数化覆盖 failure cases。

**当天产出**

- `08-production-app/tests/`

**验收测试 / 通过标准**

- [ ] 核心 deterministic 模块 coverage 目标≥80%。
- [ ] 至少 30 个测试。
- [ ] 测试不默认调用付费模型。

### Day 75 — Docker：别人能跑才算作品

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [FastAPI in Docker](https://fastapi.tiangolo.com/deployment/docker/)
- [Docker Python Guide](https://docs.docker.com/guides/python/)

**今天学什么**

- 学习 Dockerfile、layer cache、non-root 基本思路、env injection。

**今天动手做什么**

- 构建镜像。
- 写 `.env.example`，不打包 secrets。

**当天产出**

- `08-production-app/Dockerfile` + `docker-compose.yml`（可选）

**验收测试 / 通过标准**

- [ ] `docker build` 成功。
- [ ] 容器内 health endpoint 正常。
- [ ] 镜像中无真实 API key。

### Day 76 — Observability：定义运行指标，不只保存日志

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [OpenAI Agents SDK Tracing](https://openai.github.io/openai-agents-python/tracing/)
- [LangSmith Evaluation](https://docs.langchain.com/langsmith/evaluation)

**今天学什么**

- 定义 latency、model calls、tool calls、retry、HITL rate、success rate、cost proxy。

**今天动手做什么**

- 实现结构化 run summary。
- 为每个 run 生成 metrics。

**当天产出**

- `08-production-app/observability/`

**验收测试 / 通过标准**

- [ ] 任一 run 可回答“慢在哪里、失败在哪里、调用多少次”。

### Day 77 — Week 11 Production Gate：从新环境启动系统

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [FastAPI Deployment Concepts](https://fastapi.tiangolo.com/deployment/concepts/)

**今天学什么**

- 不新增内容。

**今天动手做什么**

- 模拟新用户：按 README 安装、启动 API、提交 run、触发 HITL、resume、导出结果。

**当天产出**

- `reports/production-smoke-test.md`

**验收测试 / 通过标准**

- [ ] 冷启动流程可复现。
- [ ] 关键路径 smoke test 自动化。
- [ ] 出现服务错误时有可定位日志。

---

## Week 12 — 作品集、系统设计与求职验收

### Day 78 — 现代 Agent Harness 视角：重新审视你 12 周做的东西

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Agent Learning Hub](https://github.com/datawhalechina/Agent-Learning-Hub)
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)

**今天学什么**

- 重点读 Agent Learning Hub 的 modern harness / evaluation / ship real agent 部分。
- 快速看 OpenAI Agents SDK primitives：agents、tools、handoffs、guardrails、tracing。

**今天动手做什么**

- 写“Literature Agent Harness Anatomy”：loop、tools、permission gate、state、context、trace、eval。

**当天产出**

- `portfolio/harness_anatomy.md`

**验收测试 / 通过标准**

- [ ] 能指出项目中每一层对应代码位置。
- [ ] 能说明仍缺失哪些生产能力。

### Day 79 — README 作品集化：让面试官 3 分钟理解价值

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Ch16](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter16/%E7%AC%AC%E5%8D%81%E5%85%AD%E7%AB%A0%20%E6%AF%95%E4%B8%9A%E8%AE%BE%E8%AE%A1.md)
- [Agent Learning Hub](https://github.com/datawhalechina/Agent-Learning-Hub)

**今天学什么**

- 参考毕业设计与 Project Ladder 的完整性要求。

**今天动手做什么**

- README 必含：问题、为何 Agent、架构、quickstart、demo、eval、baseline、failure cases、limitations。

**当天产出**

- `08-production-app/README.md`

**验收测试 / 通过标准**

- [ ] 陌生人按 quickstart 可启动。
- [ ] 首屏 60 秒能理解项目。
- [ ] 禁止只写技术栈列表。

### Day 80 — Architecture Decision Records：证明你会做取舍

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview)
- [LangChain Multi-Agent](https://docs.langchain.com/oss/python/langchain/multi-agent)

**今天学什么**

- 复盘所有重大选择。

**今天动手做什么**

- 至少写 4 篇 ADR：为何 Agent、为何 LangGraph、为何/为何不 Multi-Agent、为何 MCP。

**当天产出**

- `08-production-app/docs/adr/`

**验收测试 / 通过标准**

- [ ] 每篇有 Context/Decision/Alternatives/Consequences。
- [ ] 至少一篇记录“拒绝某个更复杂方案”。

### Day 81 — Agent System Design 面试：45 分钟白板

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Hello-Agents Interview Questions](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra01-%E9%9D%A2%E8%AF%95%E9%97%AE%E9%A2%98%E6%80%BB%E7%BB%93.md)
- [OpenAI Practical Guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)

**今天学什么**

- 选择 10 道系统设计题。
- 重点回答 requirements → boundary → tools → state → eval → safety → observability。

**今天动手做什么**

- 完成一次“企业文献抽取 Agent”白板设计。
- 限时 45 分钟。

**当天产出**

- `portfolio/system_design_interview.md`

**验收测试 / 通过标准**

- [ ] 必须先澄清成功标准。
- [ ] 必须包含 failure modes。
- [ ] 必须说明为何不用全多 Agent。

### Day 82 — Agent Debugging 面试：从 Trace 定位，而不是改 Prompt 碰运气

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [LangSmith Trajectory Evals](https://docs.langchain.com/langsmith/trajectory-evals)
- [Hello-Agents Interview Questions](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra01-%E9%9D%A2%E8%AF%95%E9%97%AE%E9%A2%98%E6%80%BB%E7%BB%93.md)

**今天学什么**

- 训练 8 类故障：wrong tool、bad args、retrieval miss、loop、state leak、context overflow、judge drift、timeout。

**今天动手做什么**

- 制作 8 张故障卡：症状、证据、root cause、fix、regression test。

**当天产出**

- `portfolio/debugging_cards.md`

**验收测试 / 通过标准**

- [ ] 随机抽 5 张，5 分钟内给排查顺序。
- [ ] 每个修复都附 regression test。

### Day 83 — 求职材料：把项目写成结果，不写“学习了 LangChain”

**时间预算：** 阅读 45 min｜编码 95 min｜测试 30 min｜复盘 10 min（≈3 h）

**学习网站**

- [Agent Learning Hub](https://github.com/datawhalechina/Agent-Learning-Hub)
- [Hello-Agents Interview Questions](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra01-%E9%9D%A2%E8%AF%95%E9%97%AE%E9%A2%98%E6%80%BB%E7%BB%93.md)

**今天学什么**

- 整理岗位关键词：Agent Engineer、LLM Application Engineer、AI Engineer、Research Engineer。
- 将项目表述为 problem/architecture/metric/impact。

**今天动手做什么**

- 写 3 条中文简历 bullet + 3 条英文 bullet。
- 准备 2 分钟项目介绍和 10 分钟深挖版本。

**当天产出**

- `portfolio/job_materials.md`

**验收测试 / 通过标准**

- [ ] 每条 bullet 有技术决策和量化指标占位/实值。
- [ ] 不能使用无法证明的“显著提升”。

### Day 84 — Level 5 / 全路线终极验收：模拟真实技术面试与项目交付

**时间预算：** 交付演示 90 min｜系统设计 45 min｜Debug 30 min｜总结 15 min（=3 h）

**学习网站**

- [Hello-Agents Ch16](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter16/%E7%AC%AC%E5%8D%81%E5%85%AD%E7%AB%A0%20%E6%AF%95%E4%B8%9A%E8%AE%BE%E8%AE%A1.md)
- [Agent Learning Hub](https://github.com/datawhalechina/Agent-Learning-Hub)
- [FastAPI Deployment Concepts](https://fastapi.tiangolo.com/deployment/concepts/)

**今天学什么**

- 不新增内容。

**今天动手做什么**

- 90 分钟项目交付演示：clone→run→evaluate→failure→HITL→resume。
- 45 分钟系统设计答辩。
- 30 分钟 Debugging。
- 生成最终能力矩阵和下一阶段 90 天计划。

**当天产出**

- `level-gates/final-gate.md` + GitHub-ready project

**验收测试 / 通过标准**

- [ ] 项目可运行。
- [ ] ≥80 case eval；推荐≥100。
- [ ] Single vs Multi 有数据。
- [ ] 有 trajectory eval。
- [ ] 有 FastAPI + Docker + tests。
- [ ] 有 4+ ADR。
- [ ] 能解释 Agent Loop 到 production harness 全链路。

---

# 4. 六个 Level 的硬性验收标准（汇总）

## Level 0 Gate

- [ ] 闭卷解释 Agent vs Workflow vs Chatbot。
- [ ] 闭卷解释 ReAct、Plan-and-Solve、Reflection 的机制与适用边界。
- [ ] 从空文件手写可运行 Agent Loop：tool call、observation、max_steps、timeout、error policy。
- [ ] 20-case 固定测试集可重复运行；Schema valid rate=100%。
- [ ] 能指出至少 3 个必须由确定性代码兜底的位置。

## Level 1 Gate

- [ ] 独立实现最小 Agent Harness：Message、LLM Adapter、Tool Registry、BaseAgent、ReActAgent。
- [ ] 能把自研组件逐项映射到 LangChain v1。
- [ ] LangChain single-agent extractor 可运行且拥有结构化输出。
- [ ] 自研版与 LangChain 版跑同一 dataset，有对照报告。
- [ ] 能解释何时停止维护自研框架、转向成熟框架。

## Level 2 Gate

- [ ] 能够设计非垃圾桶式 State Schema。
- [ ] Graph 至少包含 deterministic node、agentic node、conditional route、loop guard。
- [ ] Persistence/Checkpointer 可展示 state history。
- [ ] HITL 可 pause/resume。
- [ ] 故障恢复不要求整条任务从头重跑。

## Level 3 Gate

- [ ] 能比较 Router、Subagents、Handoff、Custom Workflow。
- [ ] 每个 Agent 有职责、输入/输出 schema、权限、停止条件。
- [ ] Multi-Agent 对冲突保留 provenance。
- [ ] 能检测 ping-pong / critic loop。
- [ ] Single vs Multi 使用同一 ≥50-case dataset 对照。

## Level 4 Gate

- [ ] Eval Dataset ≥80，推荐≥100。
- [ ] 至少包含 deterministic、LLM-as-judge、trajectory evaluator。
- [ ] 能从 Trace 将失败归类到 prompt/tool/retrieval/model/state/routing。
- [ ] 有 Context ablation 实验。
- [ ] MCP server/client 可运行，且能解释 MCP 与 Agent/Tool/Skill 的区别。

## Level 5 Gate

- [ ] 项目可从新环境 clone 后运行。
- [ ] FastAPI 有稳定 API contract；Docker 可启动。
- [ ] 核心 deterministic 模块有系统测试；默认测试不烧付费 API。
- [ ] README 包含 baseline、eval、failure cases、limitations。
- [ ] 至少 4 篇 ADR。
- [ ] 能完成 45 分钟 Agent System Design 与 30 分钟 Debugging 答辩。

---

# 5. 终极主项目：Multi-Agent Literature Extraction System

## 5.1 项目问题定义

面向科学与工程文献，将自然语言正文、表格描述与实验条件转为可审计结构化数据。低热水泥 / 复合胶凝材料可作为首个 benchmark 与应用场景，但不是项目身份本身：

- 组成：C3S、C2S、C3A、C4AF、SCM、外加剂等。
- 工艺：w/b、细度、养护、煅烧、龄期。
- 性能：水化热、强度、收缩、耐久、碳排。
- 证据：来源段落、表格/章节、样品 ID、单位。
- 不确定性：缺失、冲突、低置信度、人工复核。

## 5.2 推荐最终架构

```text
                         User / API
                              │
                              ▼
                       Request Classifier
                              │
                  ┌───────────┴───────────┐
                  ▼                       ▼
       Deterministic Workflow        Agentic Route
                  │                       │
                  │              ┌────────┼────────┐
                  │              ▼        ▼        ▼
                  │          Composition Property Experiment
                  │              Agent    Agent    Agent
                  │              └────────┼────────┘
                  │                       ▼
                  │                Evidence Merger
                  │                       ▼
                  │                Verifier Agent
                  │                 ┌─────┴─────┐
                  │                 ▼           ▼
                  │               PASS        ISSUE
                  │                 │           │
                  │                 │     Targeted Repair
                  │                 │           │
                  └─────────────────┼───────────┘
                                    ▼
                         Deterministic Validator
                                    │
                           ┌────────┴────────┐
                           ▼                 ▼
                        ACCEPT             HITL
                           │                 │
                           └────────┬────────┘
                                    ▼
                              Database / Export
```

## 5.3 关键设计纪律

- Agent 只负责需要语义决策的部分。
- 单位换算、Schema、范围、唯一性约束由代码处理。
- Verifier 不能无痕覆盖 Extractor。
- 所有字段保留 evidence/provenance。
- 所有循环有 budget。
- 所有架构升级必须对 baseline 做 regression。

---

# 6. 最终 Eval 指标建议

| 层级 | 指标 | 说明 |
|---|---|---|
| 字段 | Field Precision / Recall / F1 | 结构化字段正确性 |
| 数值 | Normalized Exact Match / MAE | 数值与标准单位 |
| 证据 | Evidence Precision / Coverage | 是否有真实证据支持 |
| 结构 | Schema Valid Rate | 可解析性，目标 100% |
| 工具 | Tool Selection Accuracy | 工具是否选对 |
| 参数 | Tool Argument Validity | 参数是否满足契约 |
| 轨迹 | Trajectory Match / Judge | 路径是否合理 |
| 运行 | Success Rate | 任务完成率 |
| 运行 | Avg Model Calls / Tool Calls | 调用开销 |
| 运行 | Latency P50/P95 | 延迟 |
| 运行 | Retry / HITL Rate | 系统稳定性 |
| 架构 | Single vs Multi Delta | 多 Agent 真实增益 |

---

# 7. 12 周内明确不做什么

1. **不完整精读 Hello-Agents Ch3**：你已有 Transformer/NLP 基础，只补 Agent 所需缺口。
2. **不把低代码平台作为主线**：Ch5 可课外了解，12 周主线不投入。
3. **不主攻 Agentic-RL**：Ch11 暂缓，除非未来转 Agent 训练/后训练岗位。
4. **不同时学 CrewAI、AutoGen、AgentScope、LangGraph 四套框架**：只横向理解，不并行深挖。
5. **不做“5 个角色聊天就是多 Agent”**。
6. **不把 MCP 当 Agent 框架**。
7. **不把 RAG、Memory、Context 混成一个概念**。
8. **不在没有固定 dataset 前调 prompt 宣称提升**。
9. **不使用真实 API key 写进仓库、镜像或截图**。
10. **不把天气 Agent 当核心作品集**：所有能力最终迁移到 Multi-Agent Literature Extraction System。

---

# 8. 达到什么水平可以开始投递

## 可投实习 / 初级 AI Agent / LLM Application Engineer

- Level 0–3 全通过。
- 有一个可运行 single-agent 与一个 multi-agent 对照项目。
- 会 LangGraph state/persistence/HITL。
- 有 ≥50 case eval 与失败分类。
- 能解释 tool contract、stop condition、context isolation。

## 更有竞争力

- Level 4 通过。
- ≥80/100 case regression。
- trajectory eval + trace debugging。
- MCP server/client。
- Single vs Multi 量化实验。

## 作品集可直接用于正式求职

- Level 5 通过。
- FastAPI + Docker + tests。
- GitHub README、ADR、Eval 报告完整。
- 能在白板上设计真实 Agent 系统。
- 能从 trace 排查 failure，而不是只会改 prompt。

---

# 9. 每周 Review 模板

```markdown
# Week N Review

## 1. 本周最重要的三个概念

## 2. 我之前理解错了什么

## 3. 一个成功 Case

## 4. 一个失败 Case

## 5. 失败发生在哪一层
- prompt / tool / retrieval / model / state / routing / runtime

## 6. 代码兜底在哪里生效

## 7. 当前质量 / 成本 / 延迟

## 8. 下周要验证的一个假设
```

---

# 10. 核心资源索引

- [Hello-Agents 在线阅读](https://datawhalechina.github.io/hello-agents/)
- [Hello-Agents GitHub](https://github.com/datawhalechina/hello-agents)
- [Agent Learning Hub](https://github.com/datawhalechina/Agent-Learning-Hub)
- [LangChain v1 Overview](https://docs.langchain.com/oss/python/langchain/overview)
- [LangChain Agents](https://docs.langchain.com/oss/python/langchain/agents)
- [LangChain Tools](https://docs.langchain.com/oss/python/langchain/tools)
- [LangChain Structured Output](https://docs.langchain.com/oss/python/langchain/structured-output)
- [LangChain Context Engineering](https://docs.langchain.com/oss/python/langchain/context-engineering)
- [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview)
- [Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph)
- [LangGraph Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [LangGraph Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)
- [LangGraph 101](https://github.com/langchain-ai/langgraph-101)
- [LangChain Multi-Agent](https://docs.langchain.com/oss/python/langchain/multi-agent)
- [Subagents](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents)
- [Handoffs](https://docs.langchain.com/oss/python/langchain/multi-agent/handoffs)
- [Router](https://docs.langchain.com/oss/python/langchain/multi-agent/router)
- [LangSmith Evaluation](https://docs.langchain.com/langsmith/evaluation)
- [Trajectory Evals](https://docs.langchain.com/langsmith/trajectory-evals)
- [Evaluate Complex Agent](https://docs.langchain.com/langsmith/evaluate-complex-agent)
- [MCP Introduction](https://modelcontextprotocol.io/docs/getting-started/intro)
- [Build MCP Server](https://modelcontextprotocol.io/docs/develop/build-server)
- [MCP Python SDK](https://py.sdk.modelcontextprotocol.io/)
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
- [OpenAI Agents Handoffs](https://openai.github.io/openai-agents-python/handoffs/)
- [OpenAI Agents Tracing](https://openai.github.io/openai-agents-python/tracing/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [FastAPI Async](https://fastapi.tiangolo.com/async/)
- [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [FastAPI Docker](https://fastapi.tiangolo.com/deployment/docker/)

---

# 11. 最后一条执行原则

> **每学到一个 Agent 概念，都必须回答四个问题：它解决什么失败模式？不用它会怎样？引入它增加什么复杂度？我如何用测试证明它真的有用？**

做到这一点，你形成的就不是“会用 LangChain 的人”，而是 **Agent Engineer 的系统思维**。

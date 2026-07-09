# Agent Engineering 12 周学习与求职路线

> 面向对象：已有 Python、机器学习、Transformer/NLP 基础，希望真正形成 **Agent 思维**，掌握单 Agent、多 Agent、LangGraph、评估、MCP、工程化与作品集能力。
>
> 个性化主项目：**面向低热水泥 / AI4Materials 的多 Agent 文献结构化抽取系统**。
>
> 版本核验日期：**2026-07-09**。
>
> 时间约束：**每天不超过 3 小时**；默认每周 6 天主学习 + 1 天复盘。全程约 170–200 小时。

---

## 0. 先给结论：这 12 周真正要培养什么

这份计划的目标不是“会调用几个 Agent 框架 API”，而是形成以下工程判断：

1. **先判断 Workflow 还是 Agent**：路径固定就用确定性工作流；路径需要动态决策才引入 Agent。
2. **把 Agent 看成闭环系统**：`Goal → Observe → Decide → Act → Observe → Update State → Stop/Continue`。
3. **Tool 是可执行接口，不是 Prompt 装饰品**：每个工具必须有输入契约、输出契约、错误语义和副作用边界。
4. **区分 State / Context / Memory**：当前执行状态、模型当前可见上下文、跨轮持久记忆不是一回事。
5. **不迷信“自主性”**：高风险动作、不可逆动作、低置信度动作应进入 HITL 或确定性校验。
6. **所有 Agent 都必须有停止条件**：最大步数、最大成本、超时、重复轨迹检测、失败降级。
7. **确定性外壳 + 概率性核心**：Schema、正则、单位换算、数据库约束、状态机负责兜底；LLM 负责语义判断。
8. **先把单 Agent 做到可测，再考虑 Multi-Agent**：多 Agent 不是“越多越强”，而是为上下文隔离、专业分工、并行化和权限隔离服务。
9. **评估轨迹，不只评估最终答案**：最终答案正确但调用了错误工具、成本过高、循环异常，也是不合格。
10. **生产 Agent 本质上是软件系统**：需要日志、Tracing、Eval、重试、幂等、权限、部署、测试和成本治理。

---

# 一、总体 Level 设计

| Level | 周期 | 核心能力 | 主要产物 |
|---|---:|---|---|
| Level 0 | Week 1–2 | Agent 基础思维、Tool Calling、手写 Agent Loop | 无框架 `mini-agent` |
| Level 1 | Week 3–4 | LangChain v1 单 Agent、结构化输出、错误处理 | `paper-extractor-agent-v1` |
| Level 2 | Week 5–6 | LangGraph State/Node/Edge、持久化、HITL | `paper-extraction-graph-v2` |
| Level 3 | Week 7–8 | Multi-Agent 架构、Supervisor、Router、并行研究 | `paper-multi-agent-v3` |
| Level 4 | Week 9–10 | Evaluation、Tracing、Context Engineering、MCP | `agent-eval-suite` + MCP Server |
| Level 5 | Week 11–12 | API、Docker、测试、部署、作品集与面试 | 可运行的 `FIRe Literature Agent` |

**晋级规则：**每个 Level 末尾必须通过验收。未通过时，不建议继续堆框架。

---

# 二、统一的每日时间模板（≤ 3 h）

正常学习日：

```text
35–45 min   阅读官方资料，写 5–10 行概念笔记
80–100 min  独立编码，不照抄完整答案
25–35 min   测试、故障注入、查看 Trace
15–25 min   复盘：今天做了什么决策？为什么？
------------------------------------------
总计         2 h 35 min – 3 h
```

复盘日：

```text
30 min   不看资料，口述本周核心概念
45 min   从空文件重写关键代码
30 min   跑验收测试
15 min   写 failure log
--------------------------------
总计      2 h 左右
```

建议建立固定仓库：

```text
agent-engineering-roadmap/
├── 00-notes/
├── 01-mini-agent-loop/
├── 02-single-agent-extractor/
├── 03-langgraph-extractor/
├── 04-multi-agent-extractor/
├── 05-evaluation/
├── 06-mcp-server/
├── 07-production-app/
└── README.md
```

---

# Level 0 — Agent 思维与无框架 Agent Loop

## 周期

Week 1–2

## 本 Level 的目标

你必须先脱离 LangChain/LangGraph，真正理解：

- Agent 与 Chatbot 的差异
- Workflow 与 Agent 的边界
- LLM 如何选择 Tool
- Action / Observation 如何进入下一轮
- 为什么 Agent 会死循环
- 如何设置预算、终止、重试和降级
- 为什么“代码兜底”不是附属模块，而是 Agent 架构的一部分

## 主要官方资源

- Hugging Face Agents Course：<https://huggingface.co/learn/agents-course/unit1/introduction>
- HF Agents Course GitHub：<https://github.com/huggingface/agents-course>
- LangGraph：Workflows and Agents：<https://docs.langchain.com/oss/python/langgraph/workflows-agents>
- LangChain Tools：<https://docs.langchain.com/oss/python/langchain/tools>
- LangChain Structured Output：<https://docs.langchain.com/oss/python/langchain/structured-output>
- HF smolagents Introduction：<https://huggingface.co/learn/agents-course/unit2/smolagents/introduction>
- HF Code Agents：<https://huggingface.co/learn/agents-course/unit2/smolagents/code_agents>

---

## Week 1：先建立 Agent 心智模型

### Day 1 — 什么问题值得用 Agent？

**学习链接**

- <https://huggingface.co/learn/agents-course/unit1/introduction>
- <https://docs.langchain.com/oss/python/langgraph/workflows-agents>

**学习内容**

- Agent、Workflow、Chatbot 三者区别。
- 固定流程与动态决策的边界。
- 为 10 个任务判断：普通函数 / Workflow / Agent。

**当天产出**

创建 `00-notes/day01-agent-vs-workflow.md`，至少分析：

- 文献字段抽取
- 文献下载
- 表格解析
- 单位归一化
- 新闻聚合
- 旅行规划
- 邮件助手
- 自动下单
- 代码修复
- 多目标配方优化

对每个任务给出架构选择和理由。

---

### Day 2 — Agent Loop：Observe → Decide → Act

**学习链接**

- <https://huggingface.co/learn/agents-course/unit1/introduction>
- <https://github.com/huggingface/agents-course>

**学习内容**

画出最小闭环：

```text
User Goal
   ↓
Model Decision
   ↓
Tool Call / Final Answer
   ↓
Observation
   ↓
Model Decision
   ↓
...
```

**当天编码**

不用任何 Agent 框架，手写：

```python
while step < max_steps:
    decision = model(messages, tools)
    if decision.is_final:
        break
    observation = execute_tool(decision.tool_call)
    messages.append(observation)
```

先允许工具是 mock。

**当天产出**

`01-mini-agent-loop/loop_v0.py`

---

### Day 3 — Tool Contract，而不是“给模型几个函数”

**学习链接**

- <https://docs.langchain.com/oss/python/langchain/tools>

**学习内容**

每个 Tool 写清：

- name
- description
- args schema
- return schema
- exceptions
- timeout
- side effect
- idempotency

**当天编码**

实现 3 个材料文献工具：

```text
search_section(query)
get_paragraph(section_id)
normalize_unit(value, source_unit, target_unit)
```

**当天产出**

`tool_contracts.md` + 单元测试。

---

### Day 4 — Structured Output 与 Schema

**学习链接**

- <https://docs.langchain.com/oss/python/langchain/structured-output>

**学习内容**

- JSON 不是“看起来像 JSON”。
- Pydantic Schema。
- provider-native structured output 与 tool-based structured output 的概念差异。

**当天编码**

定义：

```python
class Evidence(BaseModel):
    text: str
    section: str | None

class ExtractedField(BaseModel):
    field_name: str
    value: float | str | None
    unit: str | None
    evidence: list[Evidence]
    confidence: float
```

**当天产出**

20 条构造输入，验证非法字段、非法单位、空证据如何失败。

---

### Day 5 — ReAct 思想与 Observation

**学习链接**

- <https://huggingface.co/learn/agents-course/unit1/introduction>
- <https://huggingface.co/learn/agents-course/unit2/smolagents/introduction>

**学习内容**

重点不是背 “ReAct” 名词，而是理解：

- 当前信息不足时为什么要 Action？
- Observation 如何改变下一步？
- 工具返回太长会怎样？
- 什么时候不应继续思考？

**当天编码**

给 `loop_v0.py` 增加：

- observation truncation
- max steps
- repeated action detection
- final answer condition

---

### Day 6 — 故障注入

**学习链接**

- <https://docs.langchain.com/oss/python/langgraph/workflows-agents>

**学习内容**

主动制造：

- 工具超时
- 参数错误
- 空结果
- 重复调用
- 模型返回不存在的 Tool

**当天产出**

`failure_log_week1.md`，每个失败写：

```text
现象
根因
检测方式
恢复策略
是否应重试
```

---

### Day 7 — Week 1 闭卷复盘

**不新增框架。**

**任务**

1. 不看笔记，画 Agent Loop。
2. 用 3 分钟解释 Workflow vs Agent。
3. 从空文件写一个 3-tool Agent Loop。
4. 为每次运行记录 `step_count / tool_calls / latency / result`。

**通过线**

你不能再把 Agent 解释成“能调用工具的 LLM”。

---

## Week 2：从原理过渡到轻量框架，并建立代码兜底观

### Day 8 — smolagents：看框架如何包装 Loop

**学习链接**

- <https://huggingface.co/learn/agents-course/unit2/smolagents/introduction>
- <https://github.com/huggingface/smolagents>

**学习内容**

对照自己 Day 2 的循环，定位：

- Model
- Tool
- Agent
- Memory / Log
- Stop

**当天产出**

写 `framework_mapping.md`：框架每个抽象对应你手写 Loop 的哪一部分。

---

### Day 9 — Code Agent 思维

**学习链接**

- <https://huggingface.co/learn/agents-course/unit2/smolagents/code_agents>

**学习内容**

- JSON Tool Call 与 Code Action 的差别。
- 代码执行为什么强，也为什么危险。
- sandbox、allowlist、timeout。

**当天编码**

写一个只允许：

- 加减乘除
- 单位换算
- 简单统计

的安全执行器原型。

---

### Day 10 — “LLM 抽取 + 代码兜底”第一版

**学习链接**

- <https://docs.langchain.com/oss/python/langchain/structured-output>

**当天编码**

建立：

```text
LLM extraction
   ↓
Pydantic validation
   ↓
unit normalization
   ↓
cross-field rules
   ↓
accept / retry / manual_review
```

规则示例：

- `water_binder_ratio` 不允许负数。
- 抗压强度单位归一成 MPa。
- 养护龄期必须附带 d/h。
- 数值没有 Evidence 时降置信度。

---

### Day 11 — 终止策略与预算策略

**学习链接**

- <https://docs.langchain.com/oss/python/langgraph/workflows-agents>

**当天编码**

增加：

```text
max_steps
max_tool_calls
max_retries_per_tool
wall_clock_timeout
estimated_cost_budget
same_action_limit
```

**当天产出**

`budget_policy.md`

---

### Day 12 — 设计你的文献抽取 Agent V0

**学习链接**

- <https://github.com/langchain-ai/agents-from-scratch>

**任务**

只画架构，不急着堆代码：

```text
Input text
  ↓
Field request
  ↓
Search evidence
  ↓
Extract
  ↓
Validate
  ↓
Retry / Accept / Human Review
```

明确哪些步骤：

- 确定性
- LLM 决策
- Tool
- Validator

---

### Day 13 — 20 条小型测试集

**任务**

手工建立 `tests/data/extraction_cases.jsonl`：

- 5 条简单正文
- 5 条单位混乱
- 3 条缺失字段
- 3 条冲突数据
- 2 条表格转文本
- 2 条故意诱导幻觉

**当天产出**

初始 baseline：

- schema validity
- field exact match
- evidence presence
- tool calls

---

### Day 14 — Level 0 验收

## Level 0 硬性验收标准

必须全部满足：

- [ ] 能在 5 分钟内解释 Agent、Workflow、Tool Calling 的区别。
- [ ] 不用 LangChain/LangGraph，实现一个最小 Agent Loop。
- [ ] 至少 3 个工具，具有参数校验和异常处理。
- [ ] 有 `max_steps` 和至少 2 种异常停止策略。
- [ ] 能检测重复 Action。
- [ ] 结构化输出经过 Pydantic 验证。
- [ ] 有 20 条测试输入。
- [ ] 能明确指出系统中哪些部分应该由代码兜底。

**面试式验收题**

> “为什么不是所有复杂任务都应该用 Agent？你的文献抽取系统哪里应该是 Workflow，哪里应该是 Agent？”

要求你能连续回答 5 分钟，并画图。

---

# Level 1 — LangChain v1 单 Agent 工程能力

## 周期

Week 3–4

## 本 Level 的目标

掌握现代 LangChain 的最小必要知识：

- `create_agent`
- Models / Messages
- Tools
- Structured Output
- Middleware
- Streaming
- Short-term Memory
- Context Engineering 初步

**原则：不学习大量旧版 Chain API，不背历史包袱。**

## 主要官方资源

- LangChain Overview：<https://docs.langchain.com/oss/python/langchain/overview>
- Agents：<https://docs.langchain.com/oss/python/langchain/agents>
- Tools：<https://docs.langchain.com/oss/python/langchain/tools>
- Structured Output：<https://docs.langchain.com/oss/python/langchain/structured-output>
- Context Engineering：<https://docs.langchain.com/oss/python/langchain/context-engineering>
- Short-term Memory：<https://docs.langchain.com/oss/python/langchain/short-term-memory>
- LangGraph 101 Repo：<https://github.com/langchain-ai/langgraph-101>

---

## Week 3：单 Agent 基础

### Day 15 — LangChain v1 心智模型

**学习链接**

- <https://docs.langchain.com/oss/python/langchain/overview>
- <https://docs.langchain.com/oss/python/langchain/agents>

**任务**

用自己的话解释：

```text
Model + Prompt + Tools + Middleware + State = Agent Harness
```

**当天编码**

做一个最小 `create_agent`，只有一个 calculator tool。

---

### Day 16 — Tools 重构

**学习链接**

- <https://docs.langchain.com/oss/python/langchain/tools>

**任务**

把 Level 0 的 3 个材料工具迁移为 LangChain Tools。

**要求**

- 类型注解完整
- docstring 精确
- Tool 输入不允许“一坨字符串”
- 测试错误参数

---

### Day 17 — Structured Output 正式接入

**学习链接**

- <https://docs.langchain.com/oss/python/langchain/structured-output>

**任务**

将抽取结果改成：

```text
PaperExtraction
├── paper_id
├── fields[]
│   ├── name
│   ├── value
│   ├── unit
│   ├── evidence[]
│   └── confidence
└── warnings[]
```

**验收**

20 条测试中 schema validity ≥ 95%。

---

### Day 18 — Streaming 与可观察的 Agent

**学习链接**

- <https://docs.langchain.com/oss/python/langchain/agents>

**任务**

输出用户可见进度事件：

```text
searching evidence...
found 3 candidate paragraphs
extracting...
validating units...
```

**思考**

区分：

- 用户进度
- 内部 Trace
- 模型私有推理

---

### Day 19 — Short-term Memory

**学习链接**

- <https://docs.langchain.com/oss/python/langchain/short-term-memory>

**任务**

实现同一 thread：

```text
用户：抽取 28d 强度
用户：再把 7d 的也加上
```

第二轮能保留任务上下文。

---

### Day 20 — Context Engineering 初步

**学习链接**

- <https://docs.langchain.com/oss/python/langchain/context-engineering>

**任务**

比较 3 种上下文：

1. 整篇论文塞进去
2. top-k 段落
3. section-aware evidence package

记录：

- token 量
- 命中率
- 幻觉
- 延迟

---

### Day 21 — Week 3 复盘

**任务**

从空目录创建：

```text
single_agent/
├── schemas.py
├── tools.py
├── agent.py
├── validators.py
└── tests/
```

不允许所有代码塞一个 notebook。

---

## Week 4：从 Demo 到可测试单 Agent

### Day 22 — Middleware

**学习链接**

- <https://github.com/langchain-ai/langgraph-101/blob/main/notebooks/101/102_middleware.ipynb>

**任务**

理解 Middleware 可以做：

- 动态 Prompt
- Tool 控制
- Guardrail
- HITL 前置
- 上下文裁剪

实现一个“低置信度时增加验证指令”的 middleware 原型。

---

### Day 23 — LangGraph 101 Notebook 预习

**学习链接**

- <https://github.com/langchain-ai/langgraph-101/blob/main/notebooks/101/101_langchain_langgraph.ipynb>

**任务**

完整运行 Notebook，但每一段回答：

> “这段代码若不用框架，我要自己实现什么？”

---

### Day 24 — Agents From Scratch：Agent 架构

**学习链接**

- <https://github.com/langchain-ai/agents-from-scratch/blob/main/notebooks/agent.ipynb>

**任务**

研究 email triage 思路，映射到文献：

```text
Email triage      → Document / Field triage
Response agent    → Extraction agent
Calendar tools    → Evidence / Parser tools
```

**当天产出**

`email_to_paper_mapping.md`

---

### Day 25 — Retry 不是无脑重复

**任务**

实现失败分类：

```text
transient_tool_error   → retry
invalid_args           → repair args
no_evidence            → broaden search
schema_error           → structured retry
conflicting_evidence   → manual review
```

**要求**

每种错误有不同恢复策略。

---

### Day 26 — 单 Agent 基准测试

**学习链接**

- <https://docs.langchain.com/langsmith/evaluation-concepts>

**任务**

将测试集扩至至少 40 条，记录：

```text
field accuracy
schema validity
evidence precision
average tool calls
average latency
failure rate
```

---

### Day 27 — 单 Agent 项目整理

**任务**

完成：

```text
02-single-agent-extractor/
├── README.md
├── pyproject.toml
├── src/
├── tests/
├── evals/
└── examples/
```

README 必须有：

- Problem
- Why Agent
- Architecture
- Tool Contracts
- Failure Modes
- Evaluation
- Limitations

---

### Day 28 — Level 1 验收

## Level 1 硬性验收标准

- [ ] 会用 LangChain v1 `create_agent`，而不是只会复制旧教程。
- [ ] 至少 4 个 typed tools。
- [ ] Pydantic 结构化输出。
- [ ] 40 条测试集。
- [ ] Schema validity ≥ 95%。
- [ ] 至少 5 类 failure taxonomy。
- [ ] Retry 策略按错误类型区分。
- [ ] 能输出 streaming progress。
- [ ] 代码按 package 组织，不是单 Notebook。
- [ ] 能解释 Context 与 Memory 的区别。

**面试式验收题**

> “一个 Agent 有 30 个工具，为什么性能可能下降？你会如何重构？”

至少给出：工具分组、动态工具暴露、Router/Subagent、描述质量、Eval 五个角度中的三个。

---

# Level 2 — LangGraph：状态、控制流、持久化与 HITL

## 周期

Week 5–6

## 本 Level 的目标

把 Agent 从“循环调用模型”升级成“可控的状态系统”。

必须掌握：

- State
- Node
- Edge
- Conditional Edge
- Reducer
- Command
- Subgraph 初步
- Checkpointer
- Store
- Interrupt
- HITL
- Durable execution 思维

## 主要官方资源

- LangGraph Overview：<https://docs.langchain.com/oss/python/langgraph/overview>
- Graph API：<https://docs.langchain.com/oss/python/langgraph/graph-api>
- Quickstart：<https://docs.langchain.com/oss/python/langgraph/quickstart>
- Workflows and Agents：<https://docs.langchain.com/oss/python/langgraph/workflows-agents>
- Persistence：<https://docs.langchain.com/oss/python/langgraph/persistence>
- Interrupts：<https://docs.langchain.com/oss/python/langgraph/interrupts>
- HITL：<https://docs.langchain.com/oss/python/langchain/human-in-the-loop>
- LangGraph 101：<https://github.com/langchain-ai/langgraph-101>

---

## Week 5：Graph 思维

### Day 29 — 为什么需要 LangGraph？

**学习链接**

- <https://docs.langchain.com/oss/python/langgraph/overview>
- <https://docs.langchain.com/oss/python/langgraph/workflows-agents>

**任务**

把单 Agent V1 中的隐式流程画成显式 Graph。

---

### Day 30 — State 设计

**学习链接**

- <https://docs.langchain.com/oss/python/langgraph/graph-api>

**任务**

设计：

```python
class ExtractionState(TypedDict):
    paper_id: str
    requested_fields: list[str]
    candidate_evidence: dict
    extracted_fields: dict
    validation_errors: list[str]
    retry_count: int
    status: str
```

**重点**

State 不应变成“什么都往里扔的大字典”。

---

### Day 31 — Node 与纯函数边界

**学习链接**

- <https://docs.langchain.com/oss/python/langgraph/quickstart>

**当天编码**

实现节点：

```text
classify_request
retrieve_evidence
extract_fields
validate_schema
normalize_units
```

每个 Node 单独测试。

---

### Day 32 — Conditional Edge

**学习链接**

- <https://docs.langchain.com/oss/python/langgraph/graph-api>

**当天编码**

```text
validate
  ├── pass → normalize
  ├── missing_evidence → retrieve
  ├── invalid_schema → reextract
  └── conflict → human_review
```

---

### Day 33 — Loop、停止与循环检测

**学习链接**

- <https://docs.langchain.com/oss/python/langgraph/workflows-agents>

**任务**

实现：

- retry counter
- route history
- repeated state fingerprint
- fail terminal state

---

### Day 34 — LangGraph 101 深入运行

**学习链接**

- <https://github.com/langchain-ai/langgraph-101/blob/main/notebooks/101/101_langchain_langgraph.ipynb>

**任务**

不要只运行。把其中一个示例改成你的材料抽取场景。

---

### Day 35 — Week 5 闭卷重构

**任务**

从空文件写一个最小 Graph：

```text
START
 ↓
retrieve
 ↓
extract
 ↓
validate
 ↙    ↘
retry  END
```

能在纸上解释 State 每次如何变化。

---

## Week 6：Persistence、HITL、完整状态系统

### Day 36 — Persistence 与 Checkpointer

**学习链接**

- <https://docs.langchain.com/oss/python/langgraph/persistence>

**任务**

让任务中断后能按 `thread_id` 恢复。

测试：

1. 运行到 validate。
2. 人工终止进程。
3. 重启。
4. 从 checkpoint 继续。

---

### Day 37 — Memory：Checkpointer vs Store

**学习链接**

- <https://docs.langchain.com/oss/python/langgraph/add-memory>
- <https://docs.langchain.com/oss/python/langgraph/persistence>

**任务**

写清：

- thread-scoped short-term state
- cross-thread long-term memory

不要把“聊天记录”当成全部 Memory。

---

### Day 38 — Interrupt

**学习链接**

- <https://docs.langchain.com/oss/python/langgraph/interrupts>

**任务**

在发现冲突证据时暂停：

```text
Paper says 52.1 MPa in text
Table says 49.8 MPa
```

返回给人工审核。

---

### Day 39 — Human-in-the-loop

**学习链接**

- <https://docs.langchain.com/oss/python/langchain/human-in-the-loop>
- <https://github.com/langchain-ai/agents-from-scratch/blob/main/notebooks/hitl.ipynb>

**任务**

支持：

```text
approve
edit
reject
respond
```

并保证恢复后状态一致。

---

### Day 40 — Agents From Scratch：Memory

**学习链接**

- <https://github.com/langchain-ai/agents-from-scratch/blob/main/notebooks/memory.ipynb>

**任务**

设计“抽取偏好记忆”：

- 用户默认要 MPa。
- 用户要求保留原始证据。
- 某字段默认从 Experimental section 优先搜索。

**禁止**

把整篇历史全部永久保存进 Prompt。

---

### Day 41 — 完成 `paper-extraction-graph-v2`

**任务**

至少包含：

```text
START
  ↓
request_router
  ↓
evidence_retriever
  ↓
extractor
  ↓
validator
  ├── valid → normalizer → END
  ├── insufficient → retriever
  ├── malformed → extractor
  └── conflict → HITL → resume
```

---

### Day 42 — Level 2 验收

## Level 2 硬性验收标准

- [ ] 自己定义 State，而不是复制示例。
- [ ] 至少 6 个 Nodes。
- [ ] 至少 3 条 Conditional routes。
- [ ] 至少 1 个合法循环。
- [ ] 有循环终止策略。
- [ ] Checkpoint 后可恢复。
- [ ] 实现 HITL pause/resume。
- [ ] Node 级别单元测试。
- [ ] Graph 级集成测试。
- [ ] 能解释 State / Context / Memory / Store / Checkpoint。

**面试式验收题**

> “为什么 LangGraph 不只是把流程画成图？它解决了哪些普通 Agent Loop 的工程问题？”

要求覆盖：控制流、状态、持久化、恢复、HITL、可测试性中的至少四项。

---

# Level 3 — Multi-Agent：架构选择，而不是 Agent 数量竞赛

## 周期

Week 7–8

## 本 Level 的目标

掌握并比较：

- Router
- Supervisor / Subagents
- Handoff
- Agent-as-Tool
- Parallel Workers
- Generator–Critic
- Planner–Executor
- Custom Workflow
- Subgraphs

核心问题：

> **什么时候拆 Agent，什么时候坚决不拆？**

## 主要官方资源

- LangChain Multi-Agent：<https://docs.langchain.com/oss/python/langchain/multi-agent>
- Subagents：<https://docs.langchain.com/oss/python/langchain/multi-agent/subagents>
- Router：<https://docs.langchain.com/oss/python/langchain/multi-agent/router>
- Personal Assistant with Subagents：<https://docs.langchain.com/oss/python/langchain/multi-agent/subagents-personal-assistant>
- LangGraph Subgraphs：<https://docs.langchain.com/oss/python/langgraph/use-subgraphs>
- LangGraph 101 Multi-Agent Notebook：<https://github.com/langchain-ai/langgraph-101/blob/main/notebooks/201/multi_agent.ipynb>
- Research Agent Notebook：<https://github.com/langchain-ai/langgraph-101/blob/main/notebooks/201/research_agent.ipynb>
- OpenAI Agents SDK Quickstart：<https://openai.github.io/openai-agents-python/quickstart/>
- OpenAI Handoffs：<https://openai.github.io/openai-agents-python/handoffs/>

---

## Week 7：Multi-Agent 模式与判断

### Day 43 — 为什么 Multi-Agent？为什么经常不需要？

**学习链接**

- <https://docs.langchain.com/oss/python/langchain/multi-agent>

**任务**

为以下原因分别举例：

- context isolation
- tool isolation
- domain specialization
- parallelism
- permission boundary
- independent evaluation

再写 3 个“不该拆”的例子。

---

### Day 44 — Router

**学习链接**

- <https://docs.langchain.com/oss/python/langchain/multi-agent/router>

**当天编码**

字段路由：

```text
composition
mechanical_property
hydration_heat
shrinkage
durability
experimental_condition
```

先只做 Router + 单独函数，不急着每类一个 Agent。

---

### Day 45 — Supervisor / Subagents

**学习链接**

- <https://docs.langchain.com/oss/python/langchain/multi-agent/subagents>
- <https://docs.langchain.com/oss/python/langchain/multi-agent/subagents-personal-assistant>

**任务**

实现：

```text
Supervisor
├── Composition Agent
├── Property Agent
└── Experimental Agent
```

**关键要求**

Supervisor 不能只是把同一大段全文重复发给每个 Agent。

---

### Day 46 — Multi-Agent Notebook

**学习链接**

- <https://github.com/langchain-ai/langgraph-101/blob/main/notebooks/201/multi_agent.ipynb>

**任务**

运行并分析：

- 谁持有上下文？
- 谁决定调用？
- 子 Agent 是 stateful 还是 stateless？
- 结果怎么回传？

---

### Day 47 — Handoff 与 Agent-as-Tool

**学习链接**

- <https://openai.github.io/openai-agents-python/handoffs/>
- <https://openai.github.io/openai-agents-python/quickstart/>

**任务**

写一页比较：

```text
Handoff
vs
Agent as Tool
```

并各做一个 2-agent 示例。

---

### Day 48 — Generator–Critic / Extractor–Verifier

**任务**

实现：

```text
Extractor Agent
   ↓
Verifier Agent
   ├── pass → accept
   └── fail → targeted feedback → extractor
```

**限制**

最多 2 次反馈循环。

**关键评估**

必须比较：单 Agent vs Extractor+Verifier。

---

### Day 49 — Week 7 架构评审

**任务**

为你的系统写 ADR：

`ADR-001-why-multi-agent.md`

必须回答：

- 单 Agent baseline 哪里失败？
- 拆分依据是什么？
- 新增 Agent 的成本是什么？
- 如何证明收益？

---

## Week 8：并行研究与完整多 Agent 文献抽取

### Day 50 — Subgraphs

**学习链接**

- <https://docs.langchain.com/oss/python/langgraph/use-subgraphs>

**任务**

把至少一个专业 Agent 实现为 Subgraph。

---

### Day 51 — Parallel Workers

**学习链接**

- <https://github.com/langchain-ai/langgraph-101/blob/main/notebooks/201/research_agent.ipynb>

**任务**

并行抽取：

```text
Worker A → composition
Worker B → strength
Worker C → heat
Worker D → curing
```

记录串行与并行延迟。

---

### Day 52 — Research Agent 思维

**学习链接**

- <https://github.com/langchain-ai/deep_research_from_scratch>
- <https://github.com/langchain-ai/langgraph-101/blob/main/notebooks/201/research_agent.ipynb>

**任务**

理解：

```text
Scope → Research → Synthesize
```

将其映射为：

```text
Field Planning → Evidence Search → Extraction Synthesis
```

---

### Day 53 — Multi-Agent 共享状态与污染问题

**学习链接**

- <https://docs.langchain.com/oss/python/langchain/multi-agent>

**任务**

设计：

- 什么信息共享？
- 什么信息隔离？
- 如何避免一个 Agent 的错误污染所有 Agent？

实现 typed handoff payload。

---

### Day 54 — 完成多 Agent V3

**目标架构**

```text
                    Request Router
                         │
              ┌──────────┼──────────┐
              ↓          ↓          ↓
       Composition   Property   Experiment
          Agent        Agent       Agent
              └──────────┼──────────┘
                         ↓
                    Synthesizer
                         ↓
                   Verifier Agent
                    /          \
                 pass          fail
                  ↓             ↓
             Code Validator   Targeted Retry
                  ↓
               Database
```

---

### Day 55 — 单 Agent vs Multi-Agent 对照实验

**必须做，不可跳过。**

至少 50 条相同测试：

| 指标 | Single | Multi |
|---|---:|---:|
| Field Accuracy | | |
| Evidence Precision | | |
| Schema Validity | | |
| Avg Tool Calls | | |
| Avg Latency | | |
| Estimated Cost | | |
| Failure Rate | | |

**晋级原则**

如果 Multi-Agent 没显著收益，你必须敢于删 Agent。

---

### Day 56 — Level 3 验收

## Level 3 硬性验收标准

- [ ] 能解释 Router、Supervisor、Handoff、Agent-as-Tool。
- [ ] 至少实现两种 Multi-Agent pattern。
- [ ] 有 typed handoff payload。
- [ ] 有专业 Agent 的上下文隔离。
- [ ] 至少一个 Subgraph。
- [ ] 至少一个并行 Worker 场景。
- [ ] Extractor–Verifier 有最大循环次数。
- [ ] 用同一测试集比较 Single vs Multi。
- [ ] 能基于数据决定是否保留 Multi-Agent。
- [ ] 有 ADR 文档。

**面试式验收题**

> “为什么多 Agent 可能比单 Agent 更差？”

必须覆盖：成本、延迟、错误传播、路由误差、上下文丢失、协调复杂度、非确定性放大中的至少五项。

---

# Level 4 — Evaluation、Tracing、Context Engineering 与 MCP

## 周期

Week 9–10

## 本 Level 的目标

这一阶段决定你是“Demo 开发者”还是“Agent Engineer”。

必须掌握：

- Offline Eval
- Online Eval 概念
- Dataset
- Deterministic evaluator
- LLM-as-judge
- Final response eval
- Trajectory eval
- Single-step eval
- Tracing
- Failure taxonomy
- Context budget
- MCP Client / Server / Tool / Resource / Prompt

## 主要官方资源

- LangSmith Evaluation：<https://docs.langchain.com/langsmith/evaluation>
- Evaluation Concepts：<https://docs.langchain.com/langsmith/evaluation-concepts>
- Evaluation Quickstart：<https://docs.langchain.com/langsmith/evaluation-quickstart>
- Evaluate Complex Agent：<https://docs.langchain.com/langsmith/evaluate-complex-agent>
- Observability：<https://docs.langchain.com/langsmith/observability>
- Agents From Scratch Evaluation：<https://github.com/langchain-ai/agents-from-scratch/blob/main/notebooks/evaluation.ipynb>
- OpenAI Tracing：<https://openai.github.io/openai-agents-python/tracing/>
- MCP Introduction：<https://modelcontextprotocol.io/docs/getting-started/intro>
- MCP Architecture：<https://modelcontextprotocol.io/docs/learn/architecture>
- HF MCP Course：<https://huggingface.co/learn/mcp-course/unit0/introduction>
- HF Context Course：<https://huggingface.co/learn/context-course/unit0/introduction>

---

## Week 9：Agent Evaluation 与 Observability

### Day 57 — 什么叫“Agent 正确”？

**学习链接**

- <https://docs.langchain.com/langsmith/evaluation-concepts>
- <https://docs.langchain.com/langsmith/evaluate-complex-agent>

**任务**

建立评价层：

```text
Final Answer
Trajectory
Single Step
System Metrics
```

---

### Day 58 — 构建正式 Eval Dataset

**学习链接**

- <https://docs.langchain.com/langsmith/evaluation-quickstart>

**任务**

把数据集扩到至少 80 条；推荐最终 100 条。

覆盖：

- happy path
- missing data
- conflicting evidence
- misleading context
- unit mismatch
- tool failure
- multi-hop evidence
- abstention

---

### Day 59 — Deterministic Evaluators

**任务**

实现：

```text
schema_validity
numeric_exact_match
numeric_tolerance
unit_correctness
evidence_nonempty
citation_contains_value
forbidden_field_hallucination
```

这些优先于 LLM-as-judge。

---

### Day 60 — LLM-as-Judge

**学习链接**

- <https://docs.langchain.com/langsmith/evaluation>
- <https://github.com/langchain-ai/agents-from-scratch/blob/main/notebooks/evaluation.ipynb>

**任务**

只用于难以确定性判断的维度：

- evidence sufficiency
- semantic consistency
- explanation quality

**要求**

写清 Judge rubric。

---

### Day 61 — Trajectory Evaluation

**学习链接**

- <https://docs.langchain.com/langsmith/evaluate-complex-agent>

**任务**

评估：

- 是否调用正确 Tool
- Tool 顺序是否合理
- 是否有重复调用
- 是否绕过 Validator
- 是否过早结束

---

### Day 62 — Tracing 与故障定位

**学习链接**

- <https://docs.langchain.com/langsmith/observability>
- <https://openai.github.io/openai-agents-python/tracing/>

**任务**

对 20 个失败样本分类：

```text
routing_error
retrieval_error
extraction_error
validation_error
tool_error
handoff_error
context_overflow
loop_error
```

---

### Day 63 — Week 9 Eval Gate

**验收任务**

提交一份：

`evaluation_report_v1.md`

至少包含：

- Dataset composition
- Metrics
- Baseline
- Current model
- Error analysis
- Cost/latency
- Next experiments

---

## Week 10：Context Engineering + MCP

### Day 64 — Context Engineering 正式学习

**学习链接**

- <https://huggingface.co/learn/context-course/unit0/introduction>
- <https://docs.langchain.com/oss/python/langchain/context-engineering>

**任务**

为每次模型调用画 Context Packet：

```text
system instructions
current task
selected evidence
state summary
tool descriptions
memory
previous observations
```

---

### Day 65 — Context Budget

**任务**

实现一个简单 budgeter：

```text
max_context_tokens
reserved_output_tokens
evidence_budget
history_budget
tool_budget
```

比较“整篇全文”与“按需证据”的效果。

---

### Day 66 — MCP 是什么，不是什么

**学习链接**

- <https://modelcontextprotocol.io/docs/getting-started/intro>
- <https://modelcontextprotocol.io/docs/learn/architecture>

**任务**

解释：

```text
Host
Client
Server
Tools
Resources
Prompts
Transport
```

明确：MCP 不是 Agent 框架。

---

### Day 67 — Hugging Face MCP Course

**学习链接**

- <https://huggingface.co/learn/mcp-course/unit0/introduction>
- <https://github.com/huggingface/mcp-course>

**任务**

完成基础部分，建立最小 Server。

---

### Day 68 — 为文献系统写 MCP Server

**任务**

暴露至少 3 个工具：

```text
search_paper_sections
get_evidence_span
normalize_material_unit
```

可选 Resource：

```text
paper://{paper_id}/metadata
paper://{paper_id}/sections
```

---

### Day 69 — MCP 接入 Agent

**学习链接**

- <https://modelcontextprotocol.io/docs/learn/architecture>

**任务**

让 Agent 不再直接 import 某些工具，而通过 MCP 访问。

记录：

- 接入复杂度
- 解耦收益
- 错误传播
- 权限边界

---

### Day 70 — Level 4 验收

## Level 4 硬性验收标准

- [ ] Eval dataset ≥ 80，推荐 100 条。
- [ ] 至少 5 个 deterministic evaluators。
- [ ] 至少 1 个 LLM-as-judge rubric。
- [ ] 能分别评估 final answer / trajectory / single step。
- [ ] 有 Trace。
- [ ] 有失败分类统计。
- [ ] 比较 cost / latency / quality。
- [ ] 能解释 Context Engineering。
- [ ] 能解释 MCP Host/Client/Server。
- [ ] 自己实现一个至少 3-tool 的 MCP Server。
- [ ] Agent 能实际调用该 MCP Server。

**面试式验收题**

> “一个 Agent 最终答案准确率 90%，为什么仍可能不能上线？”

要求从轨迹、权限、成本、延迟、不可逆副作用、长尾失败、可恢复性、监控至少谈六项。

---

# Level 5 — Production、部署、作品集与求职门槛

## 周期

Week 11–12

## 本 Level 的目标

把项目从 Notebook 变成可运行系统。

必须掌握：

- Package structure
- Config / Secret 管理
- FastAPI
- Async 基础
- Tests
- Docker
- Health check
- Logging / Tracing
- API contract
- README / Architecture Decision Records
- Demo
- Resume bullets
- Interview system design

## 主要官方资源

- LangGraph Local Server：<https://docs.langchain.com/oss/python/langgraph/local-server>
- LangGraph Deployment：<https://docs.langchain.com/oss/python/langgraph/deploy>
- FastAPI：<https://fastapi.tiangolo.com/>
- FastAPI Async：<https://fastapi.tiangolo.com/async/>
- FastAPI Testing：<https://fastapi.tiangolo.com/tutorial/testing/>
- FastAPI Docker：<https://fastapi.tiangolo.com/deployment/docker/>
- Docker Python Guide：<https://docs.docker.com/guides/python/>
- OpenAI Customer Service Agents Demo：<https://github.com/openai/openai-cs-agents-demo>
- LangGraph 101 Email Agent：<https://github.com/langchain-ai/langgraph-101/blob/main/notebooks/201/email_agent.ipynb>

---

## Week 11：生产化

### Day 71 — 项目重构

**任务**

目标目录：

```text
07-production-app/
├── pyproject.toml
├── Dockerfile
├── .env.example
├── README.md
├── src/fire_agent/
│   ├── api/
│   ├── agents/
│   ├── graphs/
│   ├── tools/
│   ├── mcp/
│   ├── schemas/
│   ├── evals/
│   ├── observability/
│   └── config/
├── tests/
└── docs/
```

---

### Day 72 — FastAPI API Contract

**学习链接**

- <https://fastapi.tiangolo.com/>

**任务**

实现：

```text
POST /v1/extractions
GET  /v1/extractions/{task_id}
POST /v1/extractions/{task_id}/resume
GET  /health
```

注意长任务不要假装同步瞬间完成。

---

### Day 73 — Async 与并发

**学习链接**

- <https://fastapi.tiangolo.com/async/>

**任务**

检查：

- 模型调用
- HTTP Tool
- DB
- 并行 worker

哪些是 I/O-bound，哪些不应阻塞事件循环。

---

### Day 74 — Testing

**学习链接**

- <https://fastapi.tiangolo.com/tutorial/testing/>
- <https://fastapi.tiangolo.com/advanced/async-tests/>

**任务**

至少：

- Tool unit tests
- Node unit tests
- Graph integration tests
- API tests
- Eval regression tests

---

### Day 75 — Docker

**学习链接**

- <https://fastapi.tiangolo.com/deployment/docker/>
- <https://docs.docker.com/guides/python/>

**任务**

完成：

```bash
docker build -t fire-agent .
docker run --env-file .env -p 8000:8000 fire-agent
```

并测试 `/health`。

---

### Day 76 — Observability 与运行指标

**学习链接**

- <https://docs.langchain.com/langsmith/observability>

**任务**

至少记录：

```text
request_id
thread_id
agent_name
step_count
tool_name
latency_ms
retry_count
status
estimated_cost
error_type
```

---

### Day 77 — Week 11 生产 Gate

**任务**

在一台干净环境中：

1. clone repo
2. copy `.env.example`
3. docker build
4. docker run
5. curl API
6. 跑测试

任何一步依赖“只有你电脑知道的秘密配置”，都算失败。

---

## Week 12：作品集、面试与求职化

### Day 78 — 阅读完整生产示例

**学习链接**

- <https://github.com/openai/openai-cs-agents-demo>
- <https://github.com/langchain-ai/langgraph-101/blob/main/notebooks/201/email_agent.ipynb>

**任务**

研究：

- backend orchestration
- UI 与 agent 事件
- handoff 可视化
- state management

写 `production_demo_review.md`。

---

### Day 79 — README 作品集化

**任务**

README 必须有：

1. Problem
2. Why agentic architecture
3. Why not pure prompt
4. Architecture diagram
5. Agent roles
6. Tool contracts
7. State model
8. Retry / HITL
9. Evaluation results
10. Cost / latency
11. Local setup
12. Docker
13. Demo
14. Limitations
15. Roadmap

---

### Day 80 — 写 Architecture Decision Records

**任务**

至少 4 篇：

```text
ADR-001 Why LangGraph
ADR-002 Why/Why-not Multi-Agent
ADR-003 Why MCP for Tool Boundary
ADR-004 Why Deterministic Validation after LLM Extraction
```

这是很强的面试材料。

---

### Day 81 — 系统设计面试训练

**任务**

不看代码，45 分钟回答：

> “设计一个每天处理 10 万篇论文、自定义字段抽取、支持人工审核的 Agent 系统。”

必须覆盖：

- ingestion
- parsing
- queue
- state
- model routing
- tools
- retries
- idempotency
- HITL
- database
- eval
- observability
- cost control
- security

---

### Day 82 — Agent Debugging 面试训练

**任务**

回答以下故障：

1. Agent 一直循环。
2. Tool 参数经常错。
3. Multi-Agent 比 Single 更差。
4. 检索正确但答案错。
5. 最终答案对但成本突然翻 5 倍。
6. Handoff 后上下文丢失。
7. HITL 恢复后重复执行副作用 Tool。
8. 测试集 95%，线上只有 70%。

每题写：检测 → 定位 → 修复 → 防回归。

---

### Day 83 — 求职材料

**任务**

准备 GitHub Profile 和简历项目描述。

建议搜索岗位关键词：

```text
AI Agent Engineer
LLM Application Engineer
Generative AI Engineer
Applied AI Engineer
AI Automation Engineer
Agentic AI Engineer
LLM Platform Engineer
Research Engineer - Agents
```

**简历项目描述必须量化**，例如：

```text
Built a LangGraph-based literature extraction system with specialized
composition/property/experiment agents, deterministic Pydantic and unit
validation, checkpointed HITL, trajectory evaluation, and MCP-based tools;
evaluated on N labeled cases and reduced X-type errors by Y% versus a
single-agent baseline.
```

不要虚构数字；只写真实实验结果。

---

### Day 84 — Level 5 / 全路线终极验收

# 最终硬性验收标准

## A. 原理

- [ ] 10 分钟白板解释 Agent Loop。
- [ ] 精确区分 Workflow / Agent。
- [ ] 精确区分 State / Context / Memory。
- [ ] 能解释 Multi-Agent 的收益与代价。
- [ ] 能解释 Handoff vs Agent-as-Tool。
- [ ] 能解释 MCP 不是 Agent Framework。

## B. 代码

- [ ] 自己写过无框架 Agent Loop。
- [ ] 有 LangChain v1 单 Agent。
- [ ] 有 LangGraph Graph。
- [ ] 有 Persistence。
- [ ] 有 HITL。
- [ ] 有 Multi-Agent。
- [ ] 有 MCP Server。
- [ ] 有 FastAPI。
- [ ] 有 Docker。

## C. 可靠性

- [ ] Eval dataset ≥ 80，推荐 ≥ 100。
- [ ] Deterministic evals ≥ 5。
- [ ] 有 trajectory eval。
- [ ] 有 failure taxonomy。
- [ ] 有 retry policy。
- [ ] 有 stop/budget policy。
- [ ] 有 trace。
- [ ] 有成本和延迟统计。

## D. 工程

- [ ] package 化。
- [ ] `.env.example`。
- [ ] unit/integration/API tests。
- [ ] Docker 一键运行。
- [ ] README 完整。
- [ ] ≥ 4 篇 ADR。
- [ ] 架构图。
- [ ] Demo 视频或 GIF。

## E. 求职

- [ ] 能做 45 分钟 Agent system design。
- [ ] 能解释 8 类常见 Agent failure。
- [ ] 能现场实现一个 typed tool。
- [ ] 能现场实现 conditional routing。
- [ ] 能解释如何评估 Agent。
- [ ] 能讲清项目的真实 trade-off，而不是只介绍框架。

---

# 三、你的终极主项目：FIRe Literature Agent

建议最终项目名可以沿用你之前的 **FIRe** 品牌。

## 项目目标

> 输入论文全文 / XML / HTML / 已解析结构，用户自定义字段，系统动态规划证据检索与抽取过程，输出带证据的结构化数据；复杂字段由专业 Agent 协作，低置信度或冲突样本进入 HITL，最后经过确定性代码验证与数据库约束。

## 推荐架构

```text
                         User Request
                              │
                              ↓
                       Request Classifier
                              │
                              ↓
                        Extraction Planner
                              │
             ┌────────────────┼────────────────┐
             ↓                ↓                ↓
       Composition Agent  Property Agent  Experiment Agent
             │                │                │
             └────────────────┼────────────────┘
                              ↓
                        Evidence Merger
                              ↓
                        Verifier Agent
                     ┌────────┴────────┐
                     ↓                 ↓
                   PASS              FAIL
                     │                 │
                     ↓                 ↓
           Deterministic Validator  Targeted Retry
                     │                 │
                     ├──── conflict ───┘
                     ↓
                    HITL
                     ↓
             Unit / Rule Validator
                     ↓
                  Database
```

## 建议的专业 Agent

### 1. Composition Agent

负责：

- C3S / C2S / C3A / C4AF
- SCM
- admixture
- chemical composition

### 2. Property Agent

负责：

- compressive strength
- hydration heat
- shrinkage
- durability

### 3. Experimental Agent

负责：

- water/binder ratio
- curing
- age
- temperature
- fineness
- test standard

### 4. Verifier Agent

只负责：

- 证据是否支持值
- 单位是否一致
- 字段是否偷换概念
- 多处证据是否冲突

### 5. Code Validator

确定性执行：

- Pydantic Schema
- unit conversion
- range check
- cross-field constraints
- duplicate detection
- database constraints

---

# 四、建议建立的 Eval 指标

## 抽取质量

```text
Field Precision
Field Recall
Field F1
Exact Match
Numeric Tolerance Accuracy
Unit Accuracy
Missing-field Abstention Accuracy
```

## 证据质量

```text
Evidence Precision
Evidence Recall
Evidence Supports Value
Section Localization Accuracy
```

## Agent 轨迹

```text
Tool Selection Accuracy
Tool Argument Validity
Unnecessary Tool Call Rate
Loop Rate
Retry Success Rate
Handoff Accuracy
Route Accuracy
```

## 系统工程

```text
P50 / P95 Latency
Average Tool Calls
Average LLM Calls
Estimated Cost per Paper
Failure Rate
Recovery Rate
HITL Rate
```

---

# 五、学习过程中明确“不做什么”

## 1. 不从旧版 LangChain 全家桶开始

你只学当前主线所需：

```text
Model
Message
Tool
Structured Output
create_agent
Middleware
Memory
LangGraph
```

## 2. 不把 AutoGen 作为主线

截至本计划核验日期，其官方仓库已标记 Maintenance Mode。可以了解历史思想，但不要投入主学习时间。

官方仓库：<https://github.com/microsoft/autogen>

需要横向扩展时，优先看：

- Microsoft Agent Framework：<https://github.com/microsoft/agent-framework>

## 3. 不同时学五个 Agent 框架

主线：

```text
LangChain v1
   ↓
LangGraph
   ↓
OpenAI Agents SDK（横向比较）
   ↓
MCP
```

## 4. 不做大量“天气 Agent”作品集

天气 Demo 只用于学习 Tool Calling。你的作品集应该围绕：

- 文献抽取
- Deep Research
- 科研知识工作流
- 多 Agent 验证
- Eval
- HITL

## 5. 不在没有 baseline 时宣称 Multi-Agent 更好

必须：

```text
Single Agent baseline
        vs
Multi-Agent candidate
```

用同一 Eval Dataset 比较。

---

# 六、达到什么程度可以开始投递？

这里不给“学完 12 周必定找到工作”的虚假承诺。更合理的判断是：

## 可开始投递初级 / 实习 / 项目型岗位的最低线

满足以下 8 项中的至少 7 项：

- [ ] 有一个非玩具 Agent 项目。
- [ ] 项目有真实 Tool/API。
- [ ] 有结构化输出和 Validation。
- [ ] 有 LangGraph 或等价状态编排。
- [ ] 有 Eval Dataset。
- [ ] 有 Trace / Error Analysis。
- [ ] 有 Docker 与 API。
- [ ] 能解释架构 trade-off。

## 更有竞争力的线

- [ ] Single vs Multi-Agent 对照实验。
- [ ] trajectory eval。
- [ ] HITL + resume。
- [ ] MCP Server。
- [ ] 成本和延迟分析。
- [ ] 100+ 测试样本。
- [ ] 一个真实领域项目：你的 AI4Materials / 低热水泥场景。
- [ ] GitHub README 与 ADR 完整。

## 研究工程 / 高阶 Agent Engineer 还需继续补

12 周之后继续：

- Distributed systems
- Queue / event-driven architecture
- PostgreSQL / Redis
- Kubernetes 基础
- Security / OAuth / permissioning
- Advanced retrieval
- Model routing
- Agent learning / RL
- Benchmark design
- Open-source contribution

---

# 七、12 周之后的进阶路线

## 路线 A：Deep Agent / Long-horizon Agent

- Deep Agents From Scratch：<https://github.com/langchain-ai/deep-agents-from-scratch>
- Open Deep Research：<https://github.com/langchain-ai/open_deep_research>
- Deep Research From Scratch：<https://github.com/langchain-ai/deep_research_from_scratch>
- LangGraph 101 Deep Agents Notebook：<https://github.com/langchain-ai/langgraph-101/blob/main/notebooks/201/deepagents.ipynb>

## 路线 B：更强 Context Engineering

- HF Context Course：<https://huggingface.co/learn/context-course/unit0/introduction>
- GitHub：<https://github.com/huggingface/context-course>

## 路线 C：第二框架横向比较

- OpenAI Agents SDK：<https://github.com/openai/openai-agents-python>
- SDK Docs：<https://openai.github.io/openai-agents-python/>
- Handoffs：<https://openai.github.io/openai-agents-python/handoffs/>
- Tracing：<https://openai.github.io/openai-agents-python/tracing/>

## 路线 D：企业级 Multi-Agent 横向扩展

- Microsoft Agent Framework：<https://github.com/microsoft/agent-framework>
- Samples：<https://github.com/microsoft/Agent-Framework-Samples>

---

# 八、每周必须提交的学习证据

建议每周 Git commit 至少包含：

```text
1. 本周概念笔记
2. 可运行代码
3. tests
4. failure log
5. 一张架构图
6. 一次 benchmark/eval 结果
7. 周复盘
```

周复盘模板：

```markdown
# Week N Review

## 1. 本周最重要的三个概念

## 2. 我之前理解错了什么

## 3. 一个成功案例

## 4. 一个失败案例

## 5. Agent 做了什么错误决策

## 6. 代码兜底在哪里生效

## 7. 下周要验证的假设

## 8. 当前质量 / 成本 / 延迟
```

---

# 九、最终建议的学习优先级

按重要性排序：

```text
Agent Loop 思维
    ↓
Tool Contract
    ↓
Structured Output
    ↓
State / Control Flow
    ↓
Evaluation
    ↓
HITL / Persistence
    ↓
Context Engineering
    ↓
Multi-Agent
    ↓
MCP
    ↓
Production / Deployment
```

注意：**Multi-Agent 不应该排在 Evaluation 前面成为你的核心信仰。**

真正能够支撑求职的能力，是你能回答：

> 为什么需要 Agent？为什么需要这个 Tool？为什么要拆 Agent？如何证明变好了？失败时如何恢复？成本是多少？上线后如何监控？

当你能用自己的项目数据回答这些问题时，你才真正具备了 Agent Engineering 的思维。

---

# 十、核心官方资源索引

## Agent 基础

- Hugging Face Agents Course：<https://huggingface.co/learn/agents-course/unit0/introduction>
- Unit 1：<https://huggingface.co/learn/agents-course/unit1/introduction>
- GitHub：<https://github.com/huggingface/agents-course>

## LangChain / LangGraph

- LangChain Overview：<https://docs.langchain.com/oss/python/langchain/overview>
- Agents：<https://docs.langchain.com/oss/python/langchain/agents>
- Tools：<https://docs.langchain.com/oss/python/langchain/tools>
- Structured Output：<https://docs.langchain.com/oss/python/langchain/structured-output>
- Context Engineering：<https://docs.langchain.com/oss/python/langchain/context-engineering>
- LangGraph Overview：<https://docs.langchain.com/oss/python/langgraph/overview>
- Graph API：<https://docs.langchain.com/oss/python/langgraph/graph-api>
- Persistence：<https://docs.langchain.com/oss/python/langgraph/persistence>
- Interrupts：<https://docs.langchain.com/oss/python/langgraph/interrupts>
- Multi-Agent：<https://docs.langchain.com/oss/python/langchain/multi-agent>
- LangGraph 101：<https://github.com/langchain-ai/langgraph-101>
- Agents From Scratch：<https://github.com/langchain-ai/agents-from-scratch>

## Evaluation / Observability

- LangSmith Evaluation：<https://docs.langchain.com/langsmith/evaluation>
- Evaluation Concepts：<https://docs.langchain.com/langsmith/evaluation-concepts>
- Evaluate Complex Agent：<https://docs.langchain.com/langsmith/evaluate-complex-agent>
- Observability：<https://docs.langchain.com/langsmith/observability>

## OpenAI Agents SDK

- GitHub：<https://github.com/openai/openai-agents-python>
- Quickstart：<https://openai.github.io/openai-agents-python/quickstart/>
- Handoffs：<https://openai.github.io/openai-agents-python/handoffs/>
- Tracing：<https://openai.github.io/openai-agents-python/tracing/>

## MCP / Context

- MCP Introduction：<https://modelcontextprotocol.io/docs/getting-started/intro>
- MCP Architecture：<https://modelcontextprotocol.io/docs/learn/architecture>
- MCP Specification：<https://modelcontextprotocol.io/specification/2025-11-25>
- HF MCP Course：<https://huggingface.co/learn/mcp-course/unit0/introduction>
- HF Context Course：<https://huggingface.co/learn/context-course/unit0/introduction>

## Production

- LangGraph Local Server：<https://docs.langchain.com/oss/python/langgraph/local-server>
- LangGraph Deployment：<https://docs.langchain.com/oss/python/langgraph/deploy>
- FastAPI：<https://fastapi.tiangolo.com/>
- FastAPI Async：<https://fastapi.tiangolo.com/async/>
- FastAPI Testing：<https://fastapi.tiangolo.com/tutorial/testing/>
- FastAPI Docker：<https://fastapi.tiangolo.com/deployment/docker/>
- Docker Python Guide：<https://docs.docker.com/guides/python/>

---

> 最后的执行原则：**每天必须有代码或评估产物；每周必须有失败分析；每个 Level 必须通过验收。** 只看视频、只跑 Notebook、只调用框架 API，都不算完成。

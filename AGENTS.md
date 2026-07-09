# Git 与 GitHub 协作规则

## 仓库边界

本仓库是独立的 Agent Engineering 学习、实践与作品集路线项目：

```text
agent-engineering-roadmap
```

它用于沉淀 12 周 Agent Engineering 学习路线、阶段项目、笔记、实验代码、评估方案和最终作品集，不与其他业务项目混合维护。

| 仓库 | 职责 |
|---|---|
| `agent-engineering-roadmap` | Agent 学习路线、笔记、mini-agent、LangChain/LangGraph 实验、多 Agent 文献抽取、评估、MCP、生产化作品集 |
| 其他业务仓库 | 具体产品、业务应用或与本路线无关的项目代码 |

推送前必须确认当前目录和远端：

```text
pwd
git remote -v
git status --short --branch
```

本仓库的 GitHub remote 优先使用 SSH，便于复用本地已配置的 GitHub 密钥：

```text
git@github.com:QyuerYuanqikun/agent-engineering-roadmap.git
```

HTTPS 地址 `https://github.com/QyuerYuanqikun/agent-engineering-roadmap.git` 仅作为网页访问或备用地址；除非用户明确要求，否则不要把本地 remote 改回 HTTPS。

如果当前目录不是 `agent-engineering-roadmap`，或者 remote 指向其他项目，不得推送本项目修改。

## 项目结构约定

当前项目以最新版 `Agent_Engineering_12_Week_Roadmap.md` 为准，目录结构为：

```text
00-notes/
01-mini-agent-loop/
02-agent-framework/
03-single-agent/
04-langgraph-extractor/
05-multi-agent/
06-evaluation/
07-context-mcp/
08-production-app/
datasets/
reports/
reviews/
level-gates/
portfolio/
```

每天的最小证据包括：一个可运行产出或可检验笔记、至少一个测试/故障注入/闭卷口述结果，以及向 `daily-log.md` 追加“学到什么、失败什么、下一步验证什么”。

## 基本原则

- Git 用于记录整个项目的路线、笔记、代码、进度和维护文档；
- 规划中的空目录也属于项目结构，应在目录内放置 `.gitkeep` 占位文件并提交；
- GitHub 仓库保持私有，除非用户明确要求修改可见性；
- 本地修改、暂存、提交和远端推送是不同操作，不能混为一谈；
- 只有用户明确提出“推送”“上传到 GitHub”或同等意思时，才允许执行 `git push`；
- 普通开发、修改文件、运行测试或创建本地提交，不代表获得推送许可；
- 推送前必须再次检查分支、提交范围、敏感信息和验证结果。

## 推送授权规则

以下表达视为明确授权：

```text
推送到 GitHub
提交并推送
上传当前修改
把这个版本推上去
```

以下表达不视为推送授权：

```text
修改代码
继续开发
保存一下
做个提交
更新进度
完成这个功能
```

如果用户只要求“提交”，默认仅创建本地 Git 提交，不执行 `git push`。

## 提交信息规范

提交信息使用中文说明，并采用：

```text
<类型>: <简洁中文说明>
```

允许的主要类型：

| 类型 | 用途 |
|---|---|
| `feat` | 新增学习项目能力、工具能力或作品集功能 |
| `fix` | 修复缺陷、错误行为或不准确内容 |
| `docs` | 修改路线、笔记、进度、设计或其他文档 |
| `refactor` | 不改变外部行为的代码重构 |
| `test` | 新增或调整测试 |
| `chore` | 工具、依赖、配置和日常维护 |
| `perf` | 性能优化 |
| `ci` | 持续集成和自动化流程 |
| `build` | 构建系统或打包方式 |
| `revert` | 回退已有提交 |

示例：

```text
docs: 初始化 Agent 工程路线规范
feat: 增加无框架 Agent Loop
fix: 修正文献字段抽取 schema
refactor: 统一工具契约定义
test: 增加单位归一化测试
chore: 初始化项目目录
```

要求：

- 标题准确描述本次提交的一个主要目的；
- 使用中文动宾短语，避免“更新一下”“修改代码”等模糊说明；
- 标题尽量不超过 50 个汉字；
- 不在同一提交中混入无关修改；
- 较复杂提交可增加正文，说明背景、关键选择、影响和迁移要求；
- 不在提交信息中写入密钥、账户、内部地址或其他敏感信息。

## 提交粒度

一次提交应当形成可理解、可回退的维护单元：

- 一个学习阶段产物及其测试和文档可以放在同一提交；
- 单纯路线、笔记或进度调整可以独立提交；
- 单纯目录结构调整可以提交 `.gitkeep`，用于保留空目录；
- 格式化、依赖升级和 Agent 行为修改尽量分开；
- 未完成且不能运行的中间状态不推送到 `main`；
- 大型或高风险改动优先使用功能分支。

建议分支命名：

```text
feature/mini-agent-loop
feature/langgraph-extractor
fix/tool-contract
docs/week-01-notes
refactor/eval-suite
```

分支名保留英文、小写和连字符，提交说明和推送总结使用中文。

## 推送前检查

每次推送前至少完成：

1. 使用 `pwd` 确认当前目录是 `agent-engineering-roadmap`；
2. 使用 `git remote -v` 确认目标远端优先为 `git@github.com:QyuerYuanqikun/agent-engineering-roadmap.git`；
3. 使用 `git status` 确认提交范围；
4. 使用 `git diff` 或 `git show` 检查实际修改；
5. 检查 `.env`、密钥、Token、账户信息和大文件没有被跟踪；
6. 执行与改动相关的测试、类型检查或构建；
7. 确认路线、进度文档和变更记录是否需要同步；
8. 确认目标分支和 GitHub 仓库可见性；
9. 获得用户本次明确推送授权后再执行 `git push`。

如果测试没有运行或存在失败，推送总结必须明确说明，不能写成“验证通过”。

## 推送说明规范

推送完成后的说明使用中文，至少包含：

```text
目标仓库和分支
提交哈希和提交标题
本次主要变更
验证情况
已知限制或风险
```

示例：

```text
已推送到 QyuerYuanqikun/agent-engineering-roadmap 的 main 分支。

提交：abc1234 docs: 初始化 Agent 工程路线规范
变更：新增项目协作规则、路线目录说明和提交规范。
验证：本次为文档变更，未运行测试。
限制：尚未实现各阶段 Agent 示例代码。
```

## 版本维护

- `main` 保存当前可维护基线；
- 学习阶段、能力状态或作品集范围变化时更新项目进度文档；
- Agent 架构、评估方法、MCP 接口或重大技术决策变化时更新对应设计文档；
- 重要里程碑可使用语义化版本标签，例如 `v0.1.0`；
- 标签只在形成明确、可验收的版本时创建；
- 不改写已经共享的提交历史，不对 `main` 使用强制推送，除非用户明确要求且已经说明风险。

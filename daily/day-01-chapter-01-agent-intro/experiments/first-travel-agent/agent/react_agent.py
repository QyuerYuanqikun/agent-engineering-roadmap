import re
from collections.abc import Callable


ToolFunction = Callable[..., str]


class ReActAgent:
    """
    简化版 ReAct Agent。

    工作循环：
    LLM -> Action -> Tool -> Observation -> LLM
    """

    def __init__(
        self,
        llm,
        tools: dict[str, ToolFunction],
        system_prompt: str,
        max_iterations: int = 5,
    ):
        self.llm = llm
        self.tools = tools
        self.system_prompt = system_prompt
        self.max_iterations = max_iterations

    def run(self, user_prompt: str) -> str:
        """
        执行 Agent 主循环。
        """

        prompt_history = [
            f"用户请求: {user_prompt}"
        ]

        for i in range(self.max_iterations):
            print(
                f"\n--- 循环 {i + 1} ---"
            )

            # 1. 构造完整上下文
            full_prompt = "\n".join(
                prompt_history
            )

            # 2. 调用 LLM
            llm_output = self.llm.generate(
                prompt=full_prompt,
                system_prompt=self.system_prompt,
            )

            # 3. 只保留第一组 Thought-Action
            llm_output = self._truncate_output(
                llm_output
            )

            print(
                f"模型输出:\n{llm_output}\n"
            )

            prompt_history.append(
                llm_output
            )

            # 4. 提取 Action
            action_str = self._extract_action(
                llm_output
            )

            if action_str is None:
                observation = (
                    "错误: 未能解析到 Action 字段。"
                    "请严格遵循 "
                    "'Thought: ... Action: ...' 格式。"
                )

                self._append_observation(
                    prompt_history,
                    observation,
                )

                continue

            # 5. 检查是否 Finish
            final_answer = self._parse_finish(
                action_str
            )

            if final_answer is not None:
                return final_answer

            # 6. 执行工具
            observation = self._execute_tool(
                action_str
            )

            # 7. 保存 Observation
            self._append_observation(
                prompt_history,
                observation,
            )

        return (
            "任务未在最大循环次数内完成。"
        )

    @staticmethod
    def _truncate_output(
        llm_output: str,
    ) -> str:
        """
        只保留第一组 Thought-Action。
        """

        pattern = (
            r"(Thought:.*?Action:.*?)"
            r"(?=\n\s*"
            r"(?:Thought:|Action:|Observation:)"
            r"|\Z)"
        )

        match = re.search(
            pattern,
            llm_output,
            re.DOTALL,
        )

        if not match:
            return llm_output.strip()

        return match.group(1).strip()

    @staticmethod
    def _extract_action(
        llm_output: str,
    ) -> str | None:
        """
        提取 Action 后面的内容。
        """

        match = re.search(
            r"Action:\s*(.*)",
            llm_output,
            re.DOTALL,
        )

        if not match:
            return None

        return match.group(1).strip()

    @staticmethod
    def _parse_finish(
        action_str: str,
    ) -> str | None:
        """
        检查是否为 Finish[...]。
        """

        match = re.fullmatch(
            r"Finish\[(.*)\]",
            action_str,
            re.DOTALL,
        )

        if not match:
            return None

        return match.group(1).strip()

    def _execute_tool(
        self,
        action_str: str,
    ) -> str:
        """
        解析并执行工具调用。
        """

        # 解析：
        # get_weather(city="Beijing")
        tool_match = re.fullmatch(
            r"(\w+)\((.*)\)",
            action_str,
            re.DOTALL,
        )

        if not tool_match:
            return (
                "错误: Action 不是合法的工具调用格式。"
            )

        tool_name = tool_match.group(1)
        args_str = tool_match.group(2)

        # 解析参数：
        # city="北京", weather="晴天"
        kwargs = dict(
            re.findall(
                r'(\w+)="([^"]*)"',
                args_str,
            )
        )

        # 检查工具
        if tool_name not in self.tools:
            return (
                f"错误: 未定义的工具 '{tool_name}'"
            )

        tool = self.tools[tool_name]

        try:
            return tool(**kwargs)

        except TypeError as e:
            return (
                f"错误: 工具参数不匹配 - {e}"
            )

        except Exception as e:
            return (
                f"错误: 工具执行失败 - {e}"
            )

    @staticmethod
    def _append_observation(
        prompt_history: list[str],
        observation: str,
    ) -> None:
        """
        将 Observation 加入历史。
        """

        observation_str = (
            f"Observation: {observation}"
        )

        print(observation_str)

        prompt_history.append(
            observation_str
        )

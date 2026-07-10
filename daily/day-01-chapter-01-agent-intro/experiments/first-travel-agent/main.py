from config import settings

from agent.llm_client import (
    OpenAICompatibleClient,
)
from agent.prompts import (
    AGENT_SYSTEM_PROMPT,
)
from agent.react_agent import (
    ReActAgent,
)

from tools.registry import (
    AVAILABLE_TOOLS,
)


def main() -> None:
    """
    程序入口。
    """

    # 1. 创建 LLM 客户端
    llm = OpenAICompatibleClient(
        model=settings.llm_model_id,
        api_key=settings.llm_api_key,
        base_url=settings.llm_base_url,
    )

    # 2. 创建 Agent
    agent = ReActAgent(
        llm=llm,
        tools=AVAILABLE_TOOLS,
        system_prompt=AGENT_SYSTEM_PROMPT,
        max_iterations=5,
    )

    # 3. 用户任务
    user_prompt = (
        "你好，请帮我查询一下今天北京的天气，"
        "然后根据天气推荐一个合适的旅游景点。"
    )

    print(
        f"用户输入: {user_prompt}"
    )

    print("=" * 40)

    # 4. 启动 Agent
    final_answer = agent.run(
        user_prompt
    )

    print("\n" + "=" * 40)

    print(
        f"最终答案:\n{final_answer}"
    )


if __name__ == "__main__":
    main()

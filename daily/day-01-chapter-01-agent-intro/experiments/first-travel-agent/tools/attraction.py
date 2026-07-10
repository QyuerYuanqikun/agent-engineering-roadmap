from tavily import TavilyClient

from config import settings


def get_attraction(city: str, weather: str) -> str:
    """
    根据城市和天气情况，
    使用 Tavily Search API 搜索景点推荐。
    """

    tavily = TavilyClient(
        api_key=settings.tavily_api_key
    )

    query = (
        f"'{city}' 在'{weather}'天气下"
        f"最值得去的旅游景点推荐及理由"
    )

    try:
        response = tavily.search(
            query=query,
            search_depth="basic",
            include_answer=True,
        )

        # 优先使用综合回答
        answer = response.get("answer")

        if answer:
            return answer

        # 如果没有 answer，则整理原始结果
        formatted_results = []

        for result in response.get("results", []):
            title = result.get(
                "title",
                "无标题",
            )

            content = result.get(
                "content",
                "无内容",
            )

            formatted_results.append(
                f"- {title}: {content}"
            )

        if not formatted_results:
            return (
                "抱歉，没有找到相关的旅游景点推荐。"
            )

        return (
            "根据搜索，为您找到以下信息:\n"
            + "\n".join(formatted_results)
        )

    except Exception as e:
        return (
            f"错误: 执行 Tavily 搜索时出现问题 - {e}"
        )

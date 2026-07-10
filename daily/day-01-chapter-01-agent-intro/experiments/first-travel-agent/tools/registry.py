from collections.abc import Callable

from tools.weather import get_weather
from tools.attraction import get_attraction


ToolFunction = Callable[..., str]


AVAILABLE_TOOLS: dict[str, ToolFunction] = {
    "get_weather": get_weather,
    "get_attraction": get_attraction,
}

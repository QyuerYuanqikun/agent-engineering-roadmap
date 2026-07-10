import requests

def get_weather(city: str) -> dict:
    """
    通过调用wttr.in的API获取指定城市的天气信息。
    """
    # API端点，我们请求JSON格式的数据
    url = f"https://wttr.in/{city}?format=j1"

    try:
        # 发起网络请求
        response = requests.get(url)
        # 检测状态码是否为200（成功）
        response.raise_for_status()
        # 解析返回的json数据
        data = response.json()

        # 提取当前天气状况
        current_condition = data['current_condition'][0]
        weather_desc = current_condition['weatherDesc'][0]['value']
        temp_c = current_condition['temp_C']

        # 格式化返回自然语言
        return f"{city}当前天气：{weather_desc}，气温：{temp_c}摄氏度"

    except requests.RequestException as e:
        # 处理网络错误
        return f"错误:查询天气时遇到网络问题 - {e}"
    except (KeyError, IndexError) as e:
        # 处理数据解析错误
        return f"错误:解析天气数据失败，可能是城市名称无效 - {e}"

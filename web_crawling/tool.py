tools = [
    {
        "type": "function",
        "function": {
            "name": "melon_chart",
            "description": "멜론 차트에서 특정 순위의 노래 정보를 얻어옵니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "rank": {
                        "type": "integer",
                        "description": "멜론 차트에서 몇 번째 곡의 정보를 얻을지 지정합니다.",
                    }
                },
                "required": ["integer"],
            },
        }
    }
]
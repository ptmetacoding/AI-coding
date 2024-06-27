tools = [
    {
        "type": "function",
        "function": {
            "name": "calc",
            "description": "수식을 계산하기 위해 사용됩니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "계산할 수식을 입력합니다.",
                    }
                },
                "required": ["string"],
            },
        }
    }
]
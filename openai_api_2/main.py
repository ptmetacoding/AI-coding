from openai import OpenAI
import gradio as gr
from openai_api_2.tool import tools
import json

def calc(expression):
    try:
        return eval(expression)
    except Exception as e:
        return "수식을 계산하는 중 오류가 발생했습니다"

def predict(message, history, system_prompt):
    # 대화 기록을 전달하기
    history_openai_format = []
    history_openai_format.append({"role": "system", "content": system_prompt})
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human})
        history_openai_format.append({"role": "assistant", "content": assistant})
    history_openai_format.append({"role": "user", "content": message})

    response = client.chat.completions.create(model='gpt-3.5-turbo',
                                              messages=history_openai_format,
                                              tools=tools,
                                              tool_choice="auto")
    # 응답을 json형태로 변환해서 dict형태로 사용하기
    response = json.loads(response.json())
    response_msg = response["choices"][0]["message"]

    output = ""
    # 만약 tool_calls가 null이 아니면
    if response_msg["tool_calls"] is not None:
        print('tool_calls:', response_msg["tool_calls"])
        available_functions = {
            "calc": calc,
        }
        calls = response_msg["tool_calls"]

        for call in calls:
            function_info = call["function"]
            function_name = function_info["name"]
            if function_name == "calc":
                function = available_functions[function_name]
                parameters = json.loads(function_info["arguments"])
                result = function(**parameters)
                expression = parameters["expression"]
                output += f"{expression}식의 값은 {result}입니다."
                break

    # 만약 content가 null이 아니면
    elif response_msg["content"] is not None:
        print('content:', response_msg["content"])
        output = response_msg["content"]

    return output

# main
if __name__ == "__main__":
    api_key = open('openai_api_key.txt').read()
    client = OpenAI(api_key=api_key)

    system_prompt_textbox = gr.Textbox(label="시스템 프롬프트", value="당신은 도움을 주는 AI입니다.")
    launcher = gr.ChatInterface(
        fn=predict,
        additional_inputs=[system_prompt_textbox]
    )
    launcher.launch(share=True)

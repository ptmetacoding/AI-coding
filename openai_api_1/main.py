from openai import OpenAI
import gradio as gr

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
                                              messages=history_openai_format)
    return response.choices[0].message.content

# main
if __name__ == "__main__":
    api_key = open('../openai_api_key.txt').read()
    client = OpenAI(api_key=api_key)

    system_prompt_textbox = gr.Textbox(label="시스템 프롬프트", value="당신은 저와 끝말잇기를 하는 챗봇입니다.")
    launcher = gr.ChatInterface(
        fn=predict,
        additional_inputs=[system_prompt_textbox]
    )
    launcher.launch(share=True)

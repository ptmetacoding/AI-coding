from openai import OpenAI
import gradio as gr
import requests
def predict(message, history):
    API_URL = "http://localhost:3000/api/v1/prediction/75a92d59-8d66-4e50-976d-fee2605b08aa"

    payload = {
        "question": message,
        "overrideConfig": {
            "systemMessagePrompt": "당신은 저와 끝말잇기를 시작한 AI입니다.",
        }
    }
    response = requests.post(API_URL, json=payload)
    return response.json()['text']
# main
if __name__ == "__main__":
    api_key = open('openai_api_key.txt').read()
    client = OpenAI(api_key=api_key)
    launcher = gr.ChatInterface(
        fn=predict,
    )
    launcher.launch(share=True)

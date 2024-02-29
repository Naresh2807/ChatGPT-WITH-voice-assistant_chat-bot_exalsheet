import openai
import gradio as gr

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = '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'
openai.api_key = api_key

def chat_with_gpt(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=200  # You can adjust this to limit the response length
        )
        return response.choices[0].text
    except Exception as e:
        print(e)
        return str(e)

def chat_bot(user_input):
    response = chat_with_gpt(user_input)
    return response

iface = gr.Interface(
    fn=chat_bot,
    inputs="text",
    outputs="text",
    layout="vertical",
    title="ChatGPT",
    description="Talk to ChatGPT powered by GPT-3.5!"
)

if __name__ == "__main__":
    print("Starting Gradio interface...")
    iface.launch()

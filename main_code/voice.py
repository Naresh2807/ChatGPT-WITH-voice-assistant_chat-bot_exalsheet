import gradio as gr
import speech_recognition as sr
import openai

# Set your OpenAI API key
openai.api_key = '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'

def listen_and_recognize():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        return user_input
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "Sorry, I'm having trouble with my speech recognition service."

def chat_with_gpt(user_input):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"You: {user_input}\nAssistant:",
        max_tokens=50
    )
    return response.choices[0].text.strip()

def main():
    print("Voice Assistant: Hello! How can I assist you today?")
    
    while True:
        user_input = listen_and_recognize()
        if "exit" in user_input.lower():
            print("Voice Assistant: Goodbye!")
            break
        
        print(f"You: {user_input}")
        
        assistant_response = chat_with_gpt(user_input)
        print(f"Voice Assistant: {assistant_response}")
def chat_with_gpt(user_input):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"You: {user_input}\nAssistant:",
        max_tokens=50
    )
    return response.choices[0].text.strip()

def voice_assistant(text_input):
    assistant_response = chat_with_gpt(text_input)
    return f"Voice Assistant: {assistant_response}"

iface = gr.Interface(
    fn=voice_assistant,
    inputs=gr.Textbox(prompt="Speak to the Voice Assistant:"),
    outputs="text"
)

iface.launch()


if __name__ == "__main__":
    main()

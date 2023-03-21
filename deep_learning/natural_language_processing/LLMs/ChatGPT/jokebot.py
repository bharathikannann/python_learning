# Description: A jokebot that uses GPT-3 to generate jokes
# Usage example: python jokebot.py --openai_key "your_openai_key"

import gradio as gr
import openai
import argparse

def jokechatbot(openai_key = "", model = "gpt-3.5-turbo"):

    openai.api_key = openai_key # OPENAI_API_KEY

    # Create a message history to keep track of the conversation
    # Initialize with a joke prompt
    message_history = [{"role":"user", "content": f"You are a jokebot. I'll specify the joke and you need to Tell me a joke."}, 
                    {"role":"assistant", "content": f"OK, I'll try."}]

    # Define a function that takes in a message and returns a response
    def predict(message, model = 'gpt-3.5-turbo'):
        message_history.append({"role":"user", "content":f"{message}"}) # add the message to the message history
        completion = openai.ChatCompletion.create(
            model = model,
            messages = message_history,
        ) # generate a response

        reply_message = completion.choices[0].message.content # get the response
        message_history.append({"role":"assistant", "content":f"{reply_message}"}) # add the response to the message history
        
        # return the response to the chatbot interface in gradio (user message, bot message)
        response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(2, len(message_history)-1, 2)]
        return response

    # Create a gradio interface
    with gr.Blocks() as demo:
        chatbot = gr.Chatbot() # create a chatbot object
        with gr.Row():         # create a row to hold the chatbot and the text box
            txt = gr.Textbox(show_label = False, placeholder="Type a message...").style(container = False) # create a text box and style it
        txt.submit(predict, txt, chatbot) # submit the text box to the predict function and display the chatbot
        # txt.submit(lambda: "", None, txt) # clear text box, python version
        txt.submit(None, None, txt, _js="() => {''}") # clear text box, javascript version

    demo.launch(share=False) # launch the interface

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--openai_key", type=str, default="")
    args = args.parse_args()
    if args.openai_key == "":
        print("Please provide your OpenAI API key")
        exit()

jokechatbot(openai_key = args.openai_key)
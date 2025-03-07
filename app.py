# app.py
# ----------------------------------------
# HERE AND NOW AI - AI Chatbot UI
# This script sets up a Gradio-powered web interface for the chatbot.
# It enables users to interact with Caramel AI, leveraging RAG-based retrieval techniques.
# ----------------------------------------

import gradio as gr
# Import the chatbot logic (modify based on the use case)
#from chatbot import chat_with_LLM
#from rag_rawtext import chat_with_rawtext
#from rag_web import chat_with_web
from rag_vectortext import chat_with_vectortext  # Using vector-based RAG retrieval

# Define logo and favicon URLs (ensure they are hosted properly in the repository)
LOGO_URL = 'https://raw.githubusercontent.com/HERE-AND-NOW-ai/rag-workshop/refs/heads/main/images/chatbot_logo.png'
FAVICON_URL = 'https://raw.githubusercontent.com/HERE-AND-NOW-ai/rag-workshop/refs/heads/main/images/favicon.ico'

# Create Gradio interface
with gr.Blocks(title="HERE AND NOW AI") as demo:
    # Display logo at the top
    gr.Image(LOGO_URL, elem_id="logo", show_label=False, height=100, width=600)

    # Chatbot interface
    chatbot = gr.Chatbot(label="Caramel AI - How Can I Assist You?")

    # User input box
    msg = gr.Textbox(placeholder="Ask Anything...")

    # Buttons for user interaction
    with gr.Row():
        clear = gr.Button("Clear")
        submit_button = gr.Button(value="Submit", variant="primary")

    # Function to handle user input and update chat history
    def user(user_message, history):
        return "", history + [[user_message, None]]

    # Function to generate a response using RAG-based retrieval
    def bot(history):
        history[-1][1] = ""  # Initialize assistant's response
        for chunk in chat_with_vectortext(history[-1][0], history[:-1]):
            history[-1][1] = chunk  # Append generated response
            yield history

    # Connect user input with bot function
    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(bot, chatbot, chatbot)
    submit_button.click(user, [msg, chatbot], [msg, chatbot], queue=False).then(bot, chatbot, chatbot)

    # Clear chat history
    clear.click(lambda: None, None, chatbot, queue=False)

# Launch Gradio app with favicon
if __name__ == "__main__":
    demo.launch(favicon_path = FAVICON_URL)
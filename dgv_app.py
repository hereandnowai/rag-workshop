import gradio as gr
from chatbot import chat_with_LLM

with gr.Blocks(title="HERE AND NOW AI") as demo:
    # Add a logo at the top
    logo_path = "https://hereandnowai.com/images/logo.png"
    gr.Image(logo_path, elem_id="logo", show_label=False, height=100, width=600)

    #the interface gr will show
    chatbot = gr.Chatbot(label="What Can I Help With ")
    
    # The user Input Box
    msg = gr.Textbox(placeholder="Ask Anything ...")

    with gr.Row():
      submit_button = gr.Button(value ="Submit",variant= "primary")
      clear = gr.Button("Clear")
      
    # user function to handle user input and history
    def user(user_message, history):
        return "", history + [[user_message, None]]
    
    # bot function to generate a response based on the conversation history
    def bot(history):
        history[-1][1] = ""
        for chunk in chat_with_LLM(history[-1][0], history[:-1]):
            history[-1][1] = chunk
            yield history
     
    # When either pressing Enter in the textbox or clicking the submit button, it triggers the conversation
    msg.submit(user, [msg, chatbot], [msg, chatbot] , queue=False).then(bot,chatbot,chatbot)
    submit_button.click(user, [msg, chatbot], [msg, chatbot] , queue=False).then(bot,chatbot,chatbot)
    
    # clear the screen
    clear.click(lambda: None, None, chatbot, queue=False)

# launch the Gradio app
if __name__ == "__main__":
    demo.launch(favicon_path="https://hereandnowai.com/images/favicon.ico")

#HERE AND NOW AI 
#UI Interface for Chat

#import gradio for UI creation
import gradio as gr
#from chatbot import chat_with_LLM
#from rag_rawtext import chat_with_rawtext
#from rag_web import chat_with_web
from rag_vectortext import chat_with_vectortext

# Create Gradio interface with Chatbot
with gr.Blocks(title="HERE AND NOW AI") as demo:
    # Add a logo at the top
    logo_path = "https://hereandnowai.com/wp-content/uploads/2025/02/2-removebg-preview-1-250x28.png"
    gr.Image(logo_path, elem_id="logo", show_label=False, height=100, width=600)

    #the interface gr will show
    chatbot = gr.Chatbot(label="What Can I Help With ")
    
    # The user Input Box
    msg = gr.Textbox(placeholder="Ask Anything ...")

    with gr.Row():
      clear = gr.Button("Clear")
      submit_button = gr.Button(value ="Submit",variant= "primary")

    # user function to handle user input and history
    def user(user_message, history):
        return "", history + [[user_message, None]]
    
    # bot function to generate a response based on the conversation history
    def bot(history):
        history[-1][1] = ""
        for chunk in chat_with_vectortext(history[-1][0], history[:-1]):
            history[-1][1] = chunk
            yield history

  
    
    # When either pressing Enter in the textbox or clicking the submit button, it triggers the conversation
    msg.submit(user, [msg, chatbot], [msg, chatbot] , queue=False).then(bot,chatbot,chatbot)
    submit_button.click(user, [msg, chatbot], [msg, chatbot] , queue=False).then(bot,chatbot,chatbot)
    
    # clear the screen
    clear.click(lambda: None, None, chatbot, queue=False)

# launch the Gradio app
if __name__ == "__main__":
    demo.launch(favicon_path="images/favicon.ico")

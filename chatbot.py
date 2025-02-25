#Hereandnow AI 
#Chatbot - Chat with memory

# import our llm communicator
from llm_communicator import Get_StreamedResponse,Get_NonStreamedResponse

#Function to chat with llm
def chat_with_LLM(message, history):
    
    messages = [{"role": "system", "content": "Your name is Caramel AI, You are an AI Teacher working for 'HERE AND NOW AI'."}]

    # Add history messages 
    for h in history:
         messages.append({"role": "user", "content": h[0]})
         if h[1]:  # Only add assistant message if it exists
             messages.append({"role": "assistant", "content": h[1]})

    # Add current message
    messages.append({"role": "user", "content": message})

    #call get_completion and get response
    completion = Get_StreamedResponse(messages)

    # Stream the response
    response = "" # Initialize empty string for streaming response
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            response += content
            yield response





"""
Test for non streaming
Content 

print(Get_NonStreamedResponse()).choices[0].message.content
"""


"""
Model -> the models name in string
temprature -> float range  0 - 1, 0 for same result and 0.1 - 1 for varied result
messages -> dictionary of chat history
stream -> bool true to ask the llm to stream data
"""                                            

#testing
# Convert history to messages format
""" Testmessages = [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Hi Iam Balaji."},
      {"role": "assistant", "content": "Hi Nice to meet you Balaji."},
      {"role": "user", "content": "what is my Balaji."}
]
content = Get_StreamedResponse(Testmessages)
for chunk in content:
    print(chunk.choices[0].delta.content)  """


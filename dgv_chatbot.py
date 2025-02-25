from llm_communicator import Get_StreamedResponse
                    
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

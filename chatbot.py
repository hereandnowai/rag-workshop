# chatbot.py
# ----------------------------------------
# This module enables an AI-powered chatbot using a Retrieval-Augmented Generation (RAG) system.
# Caramel AI, an AI Teacher at HERE AND NOW AI, interacts with users by responding to queries
# and maintaining conversation history.
# ----------------------------------------

from llm_communicator import Get_StreamedResponse

def chat_with_LLM(message, history):
    """
    Handles user interaction with Caramel AI using a conversational memory.

    Parameters:
    - message (str): The latest user query.
    - history (list): List of previous conversation exchanges (tuples of user and AI responses).

    Returns:
    - generator: Streams the AI response in real-time.
    """

    # Define Caramel AI's role explicitly
    messages = [{
        "role": "system",
        "content": (
            "You are Caramel AI, an AI Teacher working for HERE AND NOW AI - Artificial Intelligence Research Institute. "
            "Your primary role is to educate users on AI concepts, including Machine Learning, Deep Learning, "
            "Natural Language Processing, and Retrieval-Augmented Generation (RAG). "
            "You provide structured, engaging, and detailed explanations with real-world examples and code snippets where needed."
        )
    }]

    # Add conversation history to maintain context
    for h in history:
        messages.append({"role": "user", "content": h[0]})
        if h[1]:  # Only add AI's response if it exists
            messages.append({"role": "assistant", "content": h[1]})

    # Add current user query
    messages.append({"role": "user", "content": message})

    # Call LLM for completion (streaming response)
    completion = Get_StreamedResponse(messages)

    # Stream AI response back to the user
    response = ""  # Initialize an empty response string
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            response += content
            yield response

# ----------------------------------------
# End of chatbot.py
# ----------------------------------------
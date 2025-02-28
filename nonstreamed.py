# nonstreamed.py
# ----------------------------------------
# This module handles non-streamed responses from the locally hosted LLM (Llama3.2).
# Unlike the streamed version, this function waits for the entire response before returning it.
# ----------------------------------------

from openai import OpenAI

# Initialize the LLM Client (Ensure this matches `llm_communicator.py`)
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

def Get_NonStreamedResponse(messages):
    """
    Sends user messages to the LLM and retrieves a complete response in one go.

    Parameters:
    - messages (list): A list of dictionaries representing the conversation history.

    Returns:
    - str: The AI-generated response.
    """
    response = client.chat.completions.create(
        model="llama3.2:latest",
        messages=messages,
        temperature=0  # Ensures deterministic responses
    )
    return response.choices[0].message.content  # Extract the final response text

# ----------------------------------------
# Example Usage (Uncomment to Test)
# ----------------------------------------

"""
test_messages = [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": "Hi, I am Balaji."}
]

response = Get_NonStreamedResponse(test_messages)
print("AI Response:", response)
"""

# ----------------------------------------
# End of nonstreamed.py
# ----------------------------------------
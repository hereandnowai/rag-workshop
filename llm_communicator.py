# llm_communicator.py
# ----------------------------------------
# This module serves as the communication interface with an LLM (Llama3.2) hosted locally via Ollama.
# It provides functionality to send messages and receive AI-generated responses in a streamed format.
# ----------------------------------------

from openai import OpenAI

# Initialize the LLM Client
# - The LLM is hosted locally at http://localhost:11434/v1
# - "ollama" is used as the API key for authentication
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

# Define Caramel AI's role in detail
CARAMEL_AI_SYSTEM_PROMPT = """
You are Caramel AI, an AI Teacher at HERE AND NOW AI - Artificial Intelligence Research Institute. 
Your role is to provide clear, structured, and engaging explanations of Artificial Intelligence concepts 
to students, researchers, and professionals. 

Your teaching style is interactive, adaptive, and detail-oriented, ensuring learners of all backgrounds 
can grasp complex AI topics. You break down concepts into simple, understandable steps, provide 
real-world examples, and engage users with questions to reinforce learning.

Areas of expertise:
- Machine Learning (Supervised, Unsupervised, Reinforcement Learning)
- Deep Learning (Neural Networks, CNNs, RNNs, Transformers, LLMs)
- Retrieval-Augmented Generation (RAG) Systems
- Natural Language Processing (NLP)
- Computer Vision (CV)
- Generative AI & LLM Fine-tuning
- AI Ethics & Responsible AI

You respond to user queries with detailed explanations, and when applicable, provide Python code snippets, 
real-world examples, and step-by-step guides. You maintain a friendly, encouraging, and professional tone 
to foster an engaging learning experience.

If a user asks something outside AI, acknowledge it and gently steer the conversation back to AI-related topics.
"""

def Get_StreamedResponse(messages):
    """
    Sends user messages to the LLM and retrieves a streamed response.

    Parameters:
    - messages (list): A list of dictionaries representing the conversation history.

    Returns:
    - generator: A stream of responses from the LLM.
    """
    return client.chat.completions.create(
        model="llama3.2:latest",
        messages=messages,
        temperature=0,  # Ensures deterministic responses for consistency
        stream=True      # Enables real-time streamed responses
    )

# ----------------------------------------
# Example Usage (Uncomment to Test)
# ----------------------------------------

"""
test_message = [
    {"role": "system", "content": CARAMEL_AI_SYSTEM_PROMPT},  # AI's predefined role
    {"role": "user", "content": "Hi, my name is Balaji."},
    {"role": "assistant", "content": "Hello! I'm Caramel AI, your AI teacher. How can I help you learn AI today?"},
    {"role": "user", "content": "What is my name?"}
]

content = Get_StreamedResponse(test_message)
for chunk in content:
    print(chunk.choices[0].delta.content)
"""

# ----------------------------------------
# End of llm_communicator.py
# ----------------------------------------
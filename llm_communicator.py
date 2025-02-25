#import the OpenAI - A Common Standard API 
#to connect with ANY LLM including OpenSource and ClosedSource
from openai import OpenAI


#the Client Declartion and Initialisation
client = OpenAI(
    # API link for LLM where it is hosted
    base_url='http://localhost:11434/v1',
    #The API Key for Authentication
    api_key='ollama',
)

# The Communicator or the chat Completion function - For Chatting
"""
 Input -> message dictionary containing system promt, user question, and assisstant answer
 Output -> A list of streaming data from llm 
"""
def Get_StreamedResponse(messages):
    return client.chat.completions.create(
         model="llama3.2:latest", temperature=0,messages=messages,stream=True)

"""
Model -> the models name in string
temprature -> float range  0 - 1, 0 for same result and 0.1 - 1 for varied result
messages -> dictionary of chat history
stream -> bool true to ask the llm to stream data
"""                                            


#Non streamed datad
def Get_NonStreamedResponse(messages):
    return client.chat.completions.create(messages, temperature=0,messages=messages)




#==============================================================================
#testing the Get_completion
""" Testmessages = [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Hi Iam Balaji."},
    
]
content = Get_StreamedResponse(Testmessages)
for chunk in content:
    print(chunk.choices[0].delta.content) """


# Function to get embeddings from OpenAI's API
def Get_embeddings(text):
    response = client.embeddings.create(
        input=text,
        model="nomic-embed-text"  
    )
    embedding = response.data[0].embedding
    return embedding

#testing embeddings
#print(get_embeddings("test"))

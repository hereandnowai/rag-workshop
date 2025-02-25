from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1",api_key="ollama")

def Get_StreamedResponse(messages):
    return client.chat.completions.create(model="llama3.2:latest",
                                          messages=messages,temperature=0,stream=True )

""" test_message = [{"role":"system",
                 "content":" Your name is Caramel AI. Your are an AI Teacher working for HERE AND NOW AI - Artificial Intelligence Research Institute"},
                {"role":"user","content":"Hi my name is balaji"},
                {"role":"assistant","content":"Hello! I'm doing great, thanks for asking! It's wonderful to meet you and help with any questions"},
                {"role":"user","content":"what is my name"},
                ]    
content = get_streamed(test_message).choices[0].message.content
print(content) """

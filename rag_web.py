# import our llm communicator

from llm_communicator import Get_StreamedResponse

# import website communicator
from bs4 import BeautifulSoup
# to get the website content
import requests

#url we are going to extract
url = 'https://hereandnowai.com/contact/'  

def scrape_website(url):
    # Send an HTTP request to the website
    response = requests.get(url)
    
    # If request is successful, parse the content
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract relevant text from the webpage (for simplicity, we get all text in <p> tags)
        paragraphs = soup.find_all('p')
        text_content = ' '.join([para.get_text() for para in paragraphs])
        
        return text_content
    else:
        return "Failed to retrieve content from the website."
    

#Test Website content
#print(scrape_website())


#Function to chat with llm
def chat_with_web(message, history):
    
    # Initialize empty string for streaming response
    response = ""

     # Convert system prompt to messages format
     # This tell the llm what role it has to play like
     # What how to process the input and what output format It has to reply
    messages = [
        {"role": "system", "content": "You are a helpful assistant that helps answer questions based on web content."}
    ]

    # Add history messages 
    for h in history:
        messages.append({"role": "user", "content": h[0]})
        if h[1]:  # Only add assistant message if it exists
            messages.append({"role": "assistant", "content": h[1]})

    web_messages = messages    
    # Extract text from the PDF
    web_extract = scrape_website(url)
    prompt = f"Context: {web_extract}\n\nQuestion: {message}\nAnswer:"

    # Add current pdf content to message
    web_messages.append({"role": "user", "content": f"{prompt}"})
    
    # Add current message in UI screen
    messages.append({"role": "user", "content": message})

    #call get_completion and get response
    completion = Get_StreamedResponse(web_messages)

    # Stream the response
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            response += content
            yield response



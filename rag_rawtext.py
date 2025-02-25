# import our llm communicator
from llm_communicator import Get_StreamedResponse
import PyPDF2

#the path of the file we are going to ask question
pdf_path = "temp/HereandNow_AI.pdf"
#pdf Extractor - Pdf to Text converter

# Function to extract text from PDF
def extract_pdf_text(pdf_path):
    # open the pdf file , read all pages using 
    # for loop and extract text from the pdf and return the text
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    
#Test PDF to text converter
#print(extract_pdf_text(pdf_path))

#Function to chat with llm
def chat_with_rawtext(message, history):
    
    # Initialize empty string for streaming response
    response = ""

     # Convert system prompt to messages format
     # This tell the llm what role it has to play like
     # What how to process the input and what output format It has to reply
    messages = [
        {"role": "system", "content": "You are a helpful assistant that helps answer questions based on PDF content."}
    ]

    # Add history messages 
    for h in history:
        messages.append({"role": "user", "content": h[0]})
        if h[1]:  # Only add assistant message if it exists
            messages.append({"role": "assistant", "content": h[1]})



    ####
    pdf_messages = messages    
    # Extract text from the PDF
    pdf_extract = extract_pdf_text(pdf_path)
    prompt = f"Context: {pdf_extract}\n\nQuestion: {message}\nAnswer:"

    # Add current pdf content to message
    pdf_messages.append({"role": "user", "content": f"{prompt}"})
      
    # Add current message in UI
    messages.append({"role": "user", "content": message})

    

    #call get_completion and get response
    completion = Get_StreamedResponse(pdf_messages)

    # Stream the response
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            response += content
            yield response


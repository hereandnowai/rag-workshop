# import our llm communicator
from llm_communicator import Get_StreamedResponse, Get_embeddings
import PyPDF2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity



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


# Function to chunk text into smaller pieces
def chunk_text(text, chunk_size=500):
    # Split the text into smaller chunks that are around `chunk_size` characters long
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

# Function to find the most relevant chunk using cosine similarity
def find_most_relevant_chunk(question, chunks):
    question_embedding = Get_embeddings(question)
    chunk_embeddings = [Get_embeddings(chunk) for chunk in chunks]
    
    # Compute cosine similarity between the question embedding and chunk embeddings
    similarities = [cosine_similarity([question_embedding], [chunk_embedding])[0][0] for chunk_embedding in chunk_embeddings]
    
    # Find the chunk with the highest similarity score
    most_relevant_chunk_index = np.argmax(similarities)
    return chunks[most_relevant_chunk_index]



#Function to chat with llm
def chat_with_vectortext(message, history):
    
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

    pdf_messages = messages    

    # Step 1: Extract text from the PDF
    pdf_extract = extract_pdf_text(pdf_path)

    # Step 2: Chunk the PDF text into smaller pieces
    chunks = chunk_text(pdf_extract)
    
    # Step 3: Find the most relevant chunk based on the question
    relevant_chunk = find_most_relevant_chunk(message, chunks)
    #print(relevant_chunk)



    prompt = f"Context: {relevant_chunk}\n\nQuestion: {message}\nAnswer:"

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


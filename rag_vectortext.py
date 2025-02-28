# rag_vectortext.py
# ----------------------------------------
# HERE AND NOW AI - RAG System with Vector Embeddings
# This module extracts text from a PDF, converts it into vector embeddings,
# and retrieves the most relevant chunks to generate AI responses.
# ----------------------------------------

import PyPDF2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from llm_communicator import Get_StreamedResponse, Get_embeddings

# Define the path to the PDF file
PDF_PATH = "temp/HereandNow_AI.pdf"

def extract_pdf_text(pdf_path):
    """
    Extracts and returns text from a given PDF file.

    Parameters:
    - pdf_path (str): Path to the PDF file.

    Returns:
    - str: Extracted text from the PDF.
    """
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return "Error extracting text from PDF."

    return text.strip()

def chunk_text(text, chunk_size=500):
    """
    Splits text into smaller chunks for efficient embedding-based retrieval.

    Parameters:
    - text (str): The full extracted text.
    - chunk_size (int): The size of each chunk (default: 500 characters).

    Returns:
    - list: A list of text chunks.
    """
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def find_most_relevant_chunk(question, chunks):
    """
    Finds the most relevant text chunk by computing cosine similarity
    between the question embedding and precomputed chunk embeddings.

    Parameters:
    - question (str): The user query.
    - chunks (list): List of text chunks.

    Returns:
    - str: The most relevant chunk of text.
    """
    try:
        question_embedding = Get_embeddings(question)
        chunk_embeddings = [Get_embeddings(chunk) for chunk in chunks]

        # Compute cosine similarity scores
        similarities = [cosine_similarity([question_embedding], [chunk_embedding])[0][0] for chunk_embedding in chunk_embeddings]
        
        # Find and return the most relevant chunk
        most_relevant_chunk_index = np.argmax(similarities)
        return chunks[most_relevant_chunk_index]
    
    except Exception as e:
        print(f"Error computing similarity: {e}")
        return "Error retrieving relevant information."

def chat_with_vectortext(message, history):
    """
    Handles user interaction with AI using vector-embedded PDF retrieval.

    Parameters:
    - message (str): The latest user query.
    - history (list): List of previous conversation exchanges.

    Returns:
    - generator: Streams AI responses based on vectorized PDF content.
    """

    # System message defining AI's role
    messages = [
        {"role": "system", "content": "You are an AI assistant specializing in answering questions based on vectorized PDF content."}
    ]

    # Add conversation history for better context
    for h in history:
        messages.append({"role": "user", "content": h[0]})
        if h[1]:  # Only add assistant's previous response if available
            messages.append({"role": "assistant", "content": h[1]})

    # Step 1: Extract text from the PDF
    pdf_extract = extract_pdf_text(PDF_PATH)
    if "Error extracting text" in pdf_extract:
        return ["Error: Unable to retrieve content from the PDF."]

    # Step 2: Chunk the PDF text into smaller sections
    chunks = chunk_text(pdf_extract)
    
    # Step 3: Find the most relevant chunk based on the user query
    relevant_chunk = find_most_relevant_chunk(message, chunks)
    if "Error retrieving" in relevant_chunk:
        return ["Error: Could not retrieve relevant information from the document."]

    # Step 4: Construct AI prompt with retrieved content
    prompt = f"Context: {relevant_chunk}\n\nQuestion: {message}\nAnswer:"
    
    # Add retrieved content as part of the message
    messages.append({"role": "user", "content": prompt})

    # Get AI response using streamed completion
    completion = Get_StreamedResponse(messages)

    # Stream AI-generated response
    response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            response += content
            yield response

# ----------------------------------------
# End of rag_vectortext.py
# ----------------------------------------
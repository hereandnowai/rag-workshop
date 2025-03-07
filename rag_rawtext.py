# rag_rawtext.py
# ----------------------------------------
# HERE AND NOW AI - RAG System with Raw Text (PDF-based Retrieval)
# This module extracts text from a PDF document and enables AI-driven responses
# using Retrieval-Augmented Generation (RAG) techniques.
# ----------------------------------------

import PyPDF2
from llm_communicator import Get_StreamedResponse

# Define the path to the PDF file (ensure the correct file is placed in the `temp` directory)
PDF_PATH = "pdfs/About_HERE_AND_NOW_AI.pdf"


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

def chat_with_rawtext(message, history):
    """
    Handles user interaction using AI responses based on extracted PDF content.

    Parameters:
    - message (str): The latest user query.
    - history (list): List of previous conversation exchanges.

    Returns:
    - generator: Streams AI responses based on PDF content.
    """
    
    # System message defining AI's role
    messages = [
        {"role": "system", "content": "You are a knowledgeable AI assistant specializing in answering questions based on the provided PDF content."}
    ]

    # Add conversation history for context
    for h in history:
        messages.append({"role": "user", "content": h[0]})
        if h[1]:  # Only add assistant's previous response if available
            messages.append({"role": "assistant", "content": h[1]})

    # Extract text from the PDF
    pdf_extract = extract_pdf_text(PDF_PATH)
    if "Error extracting text" in pdf_extract:
        return ["Error: Unable to retrieve content from the PDF."]

    # Formulate the AI prompt with extracted content
    prompt = f"Context: {pdf_extract}\n\nQuestion: {message}\nAnswer:"
    
    # Append the extracted text as part of the message
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
# End of rag_rawtext.py
# ----------------------------------------
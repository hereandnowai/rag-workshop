# rag_web.py
# ----------------------------------------
# HERE AND NOW AI - RAG System with Web Data Retrieval
# This module extracts relevant text from a webpage and enables AI-driven responses
# using Retrieval-Augmented Generation (RAG) techniques.
# ----------------------------------------

import requests
from bs4 import BeautifulSoup
from llm_communicator import Get_StreamedResponse

# Define the target URL for scraping
URL = "https://hereandnowai.com/contact/"

def scrape_website(url):
    """
    Fetches and extracts relevant text content from a given webpage.

    Parameters:
    - url (str): The URL of the webpage to scrape.

    Returns:
    - str: Extracted text content from the webpage.
    """
    try:
        response = requests.get(url, timeout=10)  # Set a timeout for requests
        response.raise_for_status()  # Raise an error for HTTP issues

        # Parse the webpage content
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract text from all paragraph tags <p>
        paragraphs = soup.find_all("p")
        text_content = " ".join([para.get_text().strip() for para in paragraphs])

        return text_content if text_content else "No relevant content found on the webpage."
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
        return "Failed to retrieve content from the website."

def chat_with_web(message, history):
    """
    Handles user interaction with AI using real-time web data retrieval.

    Parameters:
    - message (str): The latest user query.
    - history (list): List of previous conversation exchanges.

    Returns:
    - generator: Streams AI responses based on scraped web content.
    """

    # System message defining AI's role
    messages = [
        {"role": "system", "content": "You are an AI assistant specializing in answering questions based on web content retrieved in real-time."}
    ]

    # Add conversation history for context
    for h in history:
        messages.append({"role": "user", "content": h[0]})
        if h[1]:  # Only add assistant's previous response if available
            messages.append({"role": "assistant", "content": h[1]})

    # Extract web data
    web_extract = scrape_website(URL)
    if "Failed to retrieve" in web_extract:
        return ["Error: Unable to fetch web content."]

    # Construct AI prompt with retrieved web data
    prompt = f"Context: {web_extract}\n\nQuestion: {message}\nAnswer:"
    
    # Append retrieved content as part of the message
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
# End of rag_web.py
# ----------------------------------------
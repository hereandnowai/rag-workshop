### **📁 HERE AND NOW AI — RAG Workshop Repository**  
🚀 *Build Your Own Retrieval-Augmented Generation (RAG) System from Scratch!*

---

### **📋 About the Project**  
This repository contains the complete source code and assets for the **RAG (Retrieval-Augmented Generation) Workshop** conducted by **HERE AND NOW AI** — *Artificial Intelligence Research Institute*.  

By following this workshop, you'll build an end-to-end **RAG system** using **open-source LLMs**, **Gradio** for UI, and integrate it with multiple data sources like PDFs, web pages, and vector stores.

---

### **🛠️ Features**  
✅ **LLM Integration** — Connect with open-source LLMs (LLaMA, Mistral) via Ollama.  
✅ **RAG Pipelines** —  
   - 📄 **Raw Text RAG** — Directly query PDFs.  
   - 🧠 **Vector-Based RAG** — Use embeddings and cosine similarity for improved retrieval.  
   - 🌐 **Web-Based RAG** — Extract and query content from websites.  
✅ **Gradio UI** — An intuitive chatbot interface.  
✅ **Streaming & Non-Streaming Responses** — Seamless integration with LLMs.  
✅ **Custom Branding** — HERE AND NOW AI’s logo and favicon integrated into the UI.  

---

### **📂 Repository Structure**  
```
├── llm_communicator.py       # LLM API integration (Ollama/OpenAI API compatible)  
├── chatbot.py                # Memory-enabled chatbot logic  
├── app.py                    # Gradio UI application  
├── rag_rawtext.py            # RAG pipeline using raw PDF text  
├── rag_vectortext.py         # Vector-based RAG with embeddings & cosine similarity  
├── rag_web.py                # Web scraping RAG pipeline  
├── requirements.txt          # Dependencies list  
├── temp/                     # Folder for PDFs (e.g., HereandNow_AI.pdf)  
├── images/                   # Favicon and logo assets  
└── README.md                 # Project documentation  
```

---

### **🚀 How to Run the Project**  
1. **Clone the repository:**  
   ```bash
   git clone https://github.com/HEREANDNOWAI/rag-workshop.git  
   cd rag-workshop  
   ```

2. **Set up the environment:**  
   ```bash
   python -m venv rag_env  
   # Activate virtual environment  
   # Windows  
   .\rag_env\Scripts\activate  
   # Mac/Linux  
   source rag_env/bin/activate  

   # Install dependencies  
   pip install -r requirements.txt  
   ```

3. **Run the Gradio app:**  
   ```bash
   python app.py  
   ```

4. **Access the app:**  
   Open your browser and go to:  
   ```
   http://localhost:7860/  
   ```

---

### **📖 Workshop Goals**  
- Understand the architecture of **RAG systems**.  
- Learn how to integrate **LLMs** with external data sources.  
- Build an **end-to-end AI application** using open-source tools.  
- Develop an interactive **chatbot UI** using **Gradio**.

---

### **🧩 Contributing**  
We welcome contributions! Feel free to fork this repo, suggest improvements, or open issues for bugs. 💡

---

### **📜 License**  
This project is licensed under the **MIT License** — *free to use, modify, and distribute*.

---

### **🌟 Acknowledgments**  
- **HERE AND NOW AI** — *Artificial Intelligence Research Institute*  
- Special thanks to all **RAG Workshop Participants**! 🚀

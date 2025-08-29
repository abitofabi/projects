# 🧠 Resume Analyzer using LangChain, FAISS & OpenAI

A simple yet powerful AI tool that reads resumes and answers questions about them – like a smart HR assistant! 🔍 Built using [LangChain](https://www.langchain.com/), [FAISS](https://github.com/facebookresearch/faiss), and [OpenAI](https://openai.com/) – perfect for recruiters, candidates, or anyone looking to explore GenAI with documents.

---

## 🚀 Features

- Upload any resume in `.txt` format
- Ask natural questions like:
  - "What’s their education?"
  - "Does this person know AWS?"
  - "List certifications"
- Smart document search with FAISS vector index
- OpenAI-powered Q&A using `gpt-3.5-turbo`
- Dynamic "source" checker to trace answers 🕵️‍♀️
- Easy CLI interface with toggleable source view

---

## 🧱 Tech Stack

- 🧠 **LangChain** – for building the QA pipeline
- 🧊 **FAISS** – to store and search vectorized resume chunks
- 🔓 **OpenAI API** – to understand and answer your questions
- 🐍 **Python + dotenv** – to manage secrets and logic
- 🧪 Tested on: Python 3.10

---

## 📦 Installation

### 1. **Clone the repo**

    
    git clone https://github.com/your-username/resume-analyzer.git
    cd resume-analyzer
    

### 2. **Create virtual environment**

    
    python -m venv .venv
    source .venv/bin/activate  # or .venv\Scripts\activate on Windows
    

### 3. **Install requirements**

    pip install -r requirements.txt    

### 4. **Set your OpenAI API key**

Create a file `.env` in the root folder:

    OPENAI_API_KEY=your-api-key-here
## 🚀 Usage

Once everything is set up, you can interact with the resume using:

### 1. Ingest the resume

Place your resume in plain text format inside the resume folder (e.g., abinaya.txt).

Then run:
````
python ingest.py
````

This will split the document into chunks, create embeddings, and store them in a FAISS index.

### 2. Ask questions

Use:
````
python query.py
````

You'll be prompted:
````
Ask something about the resume (type 'exit' to quit or 'source' to see sources for your last question):
````

💡 To see which sources supported the last answer, type:
```
source
```

📌 If sources are already visible in the answer, this command will only show any additional relevant ones to avoid duplication.
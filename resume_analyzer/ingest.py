# ingest.py

"""
This script loads resume documents, splits them into chunks,
generates embeddings using OpenAI, and stores them in a FAISS vector database.
"""

# Step 1: Import necessary libraries
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import os
from dotenv import load_dotenv

# Step 2: Load environment variables (for OpenAI API Key)
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Step 3: Load the resume file (assumes .txt file in data/sample_resumes/)
loader = TextLoader("data/sample-resume/resume_1.txt")
documents = loader.load()  # This loads the document into LangChain's format

# Step 4: Split document into smaller chunks for better semantic embedding
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,      # max tokens per chunk
    chunk_overlap=100    # overlap so context isn't lost between chunks
)
chunks = splitter.split_documents(documents)

# Step 5: Generate embeddings using OpenAI
embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# Step 6: Create FAISS vectorstore and store the chunks
vectorstore = FAISS.from_documents(chunks, embedding)

# Step 7: Save the vectorstore locally for future querying
vectorstore.save_local("faiss_index")

print("✅ Resume successfully ingested and stored in FAISS!")

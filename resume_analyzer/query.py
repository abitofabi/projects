# query.py
"""
This script loads the FAISS vector store created in `ingest.py`
and allows you to query the indexed resumes using OpenAI-powered semantic search.
"""

from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
import re

load_dotenv()  # This loads variables from .env into environment
# Set your OpenAI API key
#   os.environ["OPENAI_API_KEY"] = "your-api-key-here"  # Replace this before running

# Load FAISS index from disk
vectordb = FAISS.load_local("faiss_index", OpenAIEmbeddings(), allow_dangerous_deserialization=True)

# Define the retriever
retriever = vectordb.as_retriever()

# Initialize LLM
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

# Create RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# Ask your question - this gave lengthy answers
# query = input("Ask something about the resume: ")
# response = qa_chain({"query": query})
#
# # Print the result
# print("\nAnswer:", response["result"])
#
# # Optionally show the documents used to answer
# for i, doc in enumerate(response["source_documents"], 1):
#     print(f"\n--- Source {i} ---\n{doc.page_content[:500]}")
last_result = None
last_query = None
# Smart source display based on query relevance
def show_relevant_sources(query, source_docs):
    matched = []
    #query_words = set(query.lower().split()) - Didnt seperate '?' from query
    # Extract clean words from the query (alphanumeric only)
    query_words = set(re.findall(r'\b\w+\b', query.lower()))
    for i, doc in enumerate(source_docs, 1):
        content_lower = doc.page_content.lower()
        if any(word in content_lower for word in query_words):
            matched.append((i, doc.page_content.strip()))

    if matched:
        print("\n📚 Sources relevant to your question:")
        for i, content in matched:
            print(f"\n--- Source {i} ---\n{content[:500]}...")
    else:
        print("\n📚 No relevant sources found for your query.")

while True:
    query = input("\nAsk something about the resume (type 'exit' to quit or 'source' to reprint the *full text* of sources for your last question): ")
    if query.lower() == "exit":
        break

    if query.lower() == "source":
        if last_result and last_query:
            show_relevant_sources(last_query, last_result["source_documents"])
        else:
            print("⚠️ No previous answer found to show sources for.")
        continue

        # Otherwise it's a normal query
    result = qa_chain.invoke({"query": query})
    print("\nAnswer:", result["result"])

    # Save it to memory so we can show sources later if needed
    last_result = result
    last_query = query
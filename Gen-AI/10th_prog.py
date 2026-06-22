# program 10
# pip install langchain-community langchain-cohere faiss-cpu sentence-transformers pypdf
# export COHERE_API_KEY="your-api-key"
# Place IPC.pdf in the same directory before running.

import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_cohere import ChatCohere

os.environ["COHERE_API_KEY"] = os.environ.get("COHERE_API_KEY", "")

docs = PyPDFLoader("IPC.pdf").load()
embeddings = HuggingFaceEmbeddings()
db = FAISS.from_documents(docs, embeddings)

llm = ChatCohere(model="command-r-03-2024")

print("Chatbot Ready! Type 'exit' to quit.")
while True:
    q = input("You: ")
    if q.lower() == "exit":
        break
    context = "\n".join(
        doc.page_content for doc in db.similarity_search(q, k=2)
    )
    r = llm.invoke(
        f"""Answer only from the context below:
{context}
Question: {q}
If the answer is not found, say:
"I could not find the answer clearly in IPC.pdf"
"""
    )
    print(r.content)

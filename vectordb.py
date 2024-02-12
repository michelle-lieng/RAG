# Import libaries
from typing import List
from langchain_openai import OpenAIEmbeddings
from pdf_chunker import parse_pdf, text_to_docs
from langchain.vectorstores.faiss import FAISS

# Read openai key
with open('GPT_api_key.txt') as f:
    openai_api_key = f.read()

def create_vectordb(pdf_files: List[str], pdf_names: List[str], openai_api_key: str):

    """
    This function aims to index PDF files. It accepts a list of PDF file objects and their names.

    The steps outlined include:
        1. parse_pdf function - reads PDF content and cleans the data
        2. text_to_docs function - splits the text into smaller chunks suitable for embedding and indexing
        3. FAISS.from_ducments - creates embeddings from chucks and returns a FAISS index and vector db 

    Langchain's "FAISS.from_documents" method takes a lists of documents and the openapi key 
    and changes all the documents into embeddings and creates a faiss vector database and index.
    """
    
    documents = []

    for pdf_file, pdf_name in zip(pdf_files, pdf_names):
        text, filename = parse_pdf(pdf_file, pdf_name)
        documents = documents + text_to_docs(text, filename)

    # documents are the cleaned and chucked PDF data
    # this data is then turned into a vector db
    
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    db = FAISS.from_documents(documents, embeddings)
    
    return db

"""
#try function
import os
def read_pdf_files_from_folder(folder_path: str):
    pdf_files = []
    pdf_names = []
    
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            pdf_names.append(file.rstrip(".pdf"))
            pdf_files.append(os.path.join("data", file))
    return pdf_files, pdf_names

pdf_files, pdf_names = read_pdf_files_from_folder("data")   

#db = create_vectordb([r"data\insurance_tncs.pdf"], ["insurance_tncs"], openai_api_key)

db = create_vectordb(pdf_files, pdf_names, openai_api_key)

query = "Who is eligible for travel insurance?"
docs = db.similarity_search(query, k=3) #get 3 chunks

for line in docs:
    print(line)
    print("\n")

#docs[1] # can slice chunks like this -> get the 2nd chunk
#print(docs[0].page_content)
"""
# Import libaries
from io import BytesIO
from langchain.embeddings.openai import OpenAIEmbeddings
from pdf_chunker import parse_pdf, text_to_docs
from langchain.vectorstores.faiss import FAISS

"""
------------------------
Langchain's vector store 
------------------------
A common way to store and search over unstructed data is to embed it and store resulting
embedding vectors. Then embed the unstructured query (query vector) and retrieve the 
embedding vectors that are most similar to the embedded query. A vector store takes care of
storing embedded data and performing vector search for you. 

---------------------
FAISS vector database
---------------------
pip install faiss-cpu 

This is a free, open-source vector store option that can be run entirely on your local machine.
The FAISS vector database makes use of Facebook AI Similarity Search (FAISS) library.

Faiss is a library that enables efficient similarity search - the vectors can be compared 
with L2 (Euclidean) distances or dot products. This library allows us to build an index and search.

-------
Summary
-------
Applying embeddings to text captures the semantic and contextual information of the data.
Best practice is to store embeddings in a vector database so we can index it.

"""

# Read openai key
with open('GPT_api_key.txt') as f:
    API_key = f.read()

def get_index_for_pdf(pdf_files, pdf_names, openai_api_key):
    """
    
    This function aims to index PDF files. It accepts a list of PDF file objects and their names.

    The steps outlined include:
        1. parse_pdf function - reads PDF content and cleans the data
        2. text_to_docs function - splits the text into smaller chunks suitable for embedding and indexing
        3. FAISS.from_ducments - creates embeddings from chucks and returns a FAISS index 

    Langchain's "FAISS.from_documents" method takes a lists of documents and the openapi key 
    and changes all the documents into embeddings and creates a faiss vector store.

    """
    documents = []

    for pdf_path, pdf_name in zip([r"data\amex.pdf"], ["Amex"]):

        # open the PDF file in binary mode ('rb') and ensure its content is read as bytes-like object
        with open(pdf_path, 'rb') as file: 
            pdf_file = file.read()

        text, filename = parse_pdf(BytesIO(pdf_file), pdf_name)
        documents = documents + text_to_docs(text, filename)

    # documents are the cleaned and chucked PDF data
    # this data is then turned into a vector store
    
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    index = FAISS.from_documents(documents, embeddings)

    return index

# Trying the function
get_index_for_pdf(r"data\amex.pdf", "amex", API_key)

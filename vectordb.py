# Import libaries
from io import BytesIO
from langchain_openai import OpenAIEmbeddings
from pdf_chunker import parse_pdf, text_to_docs
from langchain.vectorstores.faiss import FAISS

# Read openai key
with open('GPT_api_key.txt') as f:
    openai_api_key = f.read()

def create_vectordb(pdf_files, pdf_names, openai_api_key):
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

    for pdf_path, pdf_name in zip([r"data\amex.pdf"], ["Amex"]):

        # open the PDF file in binary mode ('rb') and ensure its content is read as bytes-like object
        with open(pdf_path, 'rb') as file: 
            pdf_file = file.read()

        text, filename = parse_pdf(BytesIO(pdf_file), pdf_name)
        documents = documents + text_to_docs(text, filename)

    # documents are the cleaned and chucked PDF data
    # this data is then turned into a vector db
    
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    db = FAISS.from_documents(documents, embeddings)

    return db

# Trying the function
db = create_vectordb(r"data\amex.pdf", "amex", openai_api_key)

query = "Who is eligible for travel insurance?"
docs = db.similarity_search(query, k=3) #get 3 chunks

docs[1] # can slice chunks like this -> get the 2nd chunk
print(docs[0].page_content)
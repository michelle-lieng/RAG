# Import libraries
import re
from io import BytesIO
from typing import List # use List as then we can be specific on which elements the list can contain, e.g. List(str)
from langchain.docstore.document import Document
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def parse_pdf(file: BytesIO, filename: str) -> tuple[List[str], str]:
    """

    This function is used to:
        - Read a PDF file
        - Extract text
        - Apply text processing and cleaning operations to the text
    
    """
    # Initialize the PDF reader for the provided file
    pdf = PdfReader(file)
    cleaned_text = []
    
    # Loop through all the pages in the PDF
    for page in pdf.pages:
        # Extract the text from the page
        text = page.extract_text()
        
        # re.sub is used to find and then replace certain parts of the text to clean it up
        # replace single newlines with spaces
        text = re.sub(r"\n", " ",text)

        # for the insurance terms and conditions document - lots of cases of e.g. "Y our", "T rip", "T ravel"
        # if text has a " T " replace with " T" or " Y " replace with " Y" (basically remove space after)
        # change shouldn't affect other pdfs since T and Y are not words
        # see file docs\regex_basics.ipynb for experiementation

        text = re.sub(r" T ", r" T", text)
        text = re.sub(r" Y ", r" Y", text)
        
        # Append the cleaned text to the output list.
        cleaned_text.append(text)
    
    # Return the list of cleaned texts and the filename.
    return cleaned_text, filename

# Trialing the parse_pdf function
#pdf = PdfReader(r"data\insurance_terms_and_conditions.pdf")
#text = pdf.pages[0].extract_text()
# parse_pdf(r"data\insurance_tncs.pdf", "insurance_tncs")

def text_to_docs(text: List[str], filename: str) -> List[Document]:
    """

    Note: the text variable is a list of cleaned text where each element is a page from a pdf

    This function is used to:
        - Take a list of text strings & file name
        - Processes the text to create a list of chunked "Document" objects
        - These objects each represent a smaller portion of the original text with associated metadata
    
    """
    # Ensure the input text is a list. If it's a string, convert it to a list.
    if isinstance(text, str):
        text = [text]
    
    # Convert each text (from a page) to a Langchain Document object
    page_docs = [Document(page_content=page) for page in text]
    
    # Assign a page number to the metadata of each document.
    for i, doc in enumerate(page_docs):
        doc.metadata["page"] = 1+i #as enumerate starts at 0

    doc_chunks = []
    
    # Split each page's text into smaller chunks and store them as separate documents.
    for doc in page_docs:
        # Initialize the text splitter with specific chunk sizes and delimiters.
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000, 
            separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""],
            chunk_overlap=0,
        )
        
        # Split the dcument pages into chunks
        chunks = text_splitter.split_text(doc.page_content)
        # print(chunks)

        # Convert each chunk into a new document, storing its chunk number, page number, and source file name in its metadata.
        for i, chunk in enumerate(chunks):
            doc = Document(
                page_content=chunk, 
                metadata={"page": doc.metadata["page"], #this is the page metadata from previous doc object before it was chunked
                          "chunk": i+1}
                          )
            # doc.metadata["source"] = f"page {doc.metadata['page']} - section {doc.metadata['chunk']}"
            doc.metadata["filename"] = filename
            doc_chunks.append(doc)
    
    # Return the list of chunked documents.
    return doc_chunks

"""
# trying the functions

cleaned_text, filename = parse_pdf("data\\qantas_points_tncs.pdf", "qantas_points_tncs")
include_metadata = text_to_docs(cleaned_text,filename)

for line in include_metadata:
    print(line)
    print("\n")
"""

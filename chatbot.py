# Import libraries
import os
from vectordb import create_vectordb 
from openai import OpenAI

# Read openai key
with open('GPT_api_key.txt') as f:
    openai_api_key = f.read()

def read_pdf_files_from_folder(folder_path):
    pdf_files = []
    pdf_names = []
    
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            pdf_names.append(file.rstrip(".pdf"))
            pdf_files.append(os.path.join("data", file))
    return pdf_files, pdf_names

#read_pdf_files_from_folder("data")

# Define the template for the chatbot system prompt
system_prompt = """
    You are a helpful Assistant who answers to users questions based on multiple contexts given to you.
    Keep your answer short and to the point.
    The evidence are the context of the pdf extract with metadata. 
    Carefully focus on the metadata specially 'filename' and 'page' whenever answering.
    Make sure to add filename and page number at the end of sentence you are citing to.
    Reply "Not applicable" if text is irrelevant.
    The PDF content is:
    {pdf_extract}
"""

def chatbot(user_query: str):
    data_folder = "data"  # Path to the folder where PDFs are stored.
    pdf_files, pdf_names = read_pdf_files_from_folder(data_folder)

    # create vector database and index
    db = create_vectordb(pdf_files, pdf_names, openai_api_key)

    # retrieve 3 similar document chunks to the user query
    docs = db.similarity_search(user_query, k=3) 

    # add these document chunks to the system prompt
    pdf_extract = "/n ".join([result.page_content for result in docs])

    # call openai api
    client = OpenAI(api_key=openai_api_key)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt.format(pdf_extract=pdf_extract)},
            {"role": "user", "content": user_query}
        ]
    )

    return completion.choices[0].message.content

# tried the chatbot function
print(chatbot("Who is eligible for travel insurance?"))


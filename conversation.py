# Import libraries
import os
from vectordb import create_vectordb 
from openai import OpenAI
import json # for readability of the chat history

# Read openai key
with open('GPT_api_key.txt') as f:
    openai_api_key = f.read()

def read_pdf_files_from_folder(folder_path: str):
    pdf_files = []
    pdf_names = []
    
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            pdf_names.append(file.rstrip(".pdf"))
            pdf_files.append(os.path.join("data", file))
    return pdf_files, pdf_names


read_pdf_files_from_folder("data")

# Define the template for the chatbot system prompt
system_prompt = """
    You are a helpful assistant who answers to users questions based on multiple contexts given to you.
    Keep your answer short and to the point.
    The evidence are the context of the pdf extract with metadata. 
    Carefully focus on the metadata specially 'filename' and 'page' whenever answering.
    Make sure to add filename and page number at the end of sentence you are citing to.
    Reply "Not applicable" if text is irrelevant.
    The PDF content is:
    {pdf_extract}
"""

def conversation():
    user_query = ""  # Initialize x with an empty string
    chat_history = [] # Define chat history
    while True:
        user_query = input("Ask anything: ")
        if user_query.lower() == "end":
            break
        else:
            data_folder = "data"  # Path to the folder where PDFs are stored.
            pdf_files, pdf_names = read_pdf_files_from_folder(data_folder)

            # create vector database and index
            db = create_vectordb(pdf_files, pdf_names, openai_api_key)

            # retrieve 3 similar document chunks to the user query
            docs = db.similarity_search(user_query, k=1) 

            # add these document chunks to the system prompt
            pdf_extract = "/n ".join([result.page_content for result in docs])

            #initialize system prompt to be added to the model
            system = {"role": "system", "content": system_prompt.format(pdf_extract=pdf_extract)}

            # add in user_query to chat history 
            chat_history.append({"role": "user", "content": user_query})

            # call openai api
            client = OpenAI(api_key=openai_api_key)

            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[system] + chat_history,
                temperature=0,
                max_tokens=150,
                frequency_penalty=0
            )

            chatbot_response = completion.choices[0].message.content
            chat_history.append({"role": "assistant", "content": chatbot_response})
            
            print("\n")
            print("This is the chatbot response: ")
            print("-----------------------------")
            print(chatbot_response)
            print("\n")
            print("This is the chat history: ")
            print("-------------------------")
            for entry in chat_history:
                print(json.dumps(entry, indent=4))
            continue

conversation()

"""
Example questions to ask for AMEX document:
- How long can I be covered for while travelling?
- Are there any countries that I will not be covered for if I travel to?
- What is eligible for travel insurance?
- What am I covered for?
- What ages can I be covered by travel insurance?
"""
# Setup module paths
from chatbot_setup import setup_module_path
setup_module_path()

# Import libraries
from src.vectordb import create_vectordb 
from src.chatbot_setup import system_prompt, read_pdf_files_from_folder
from openai import OpenAI
import gradio as gr

# Read openai key
with open(r'src\GPT_api_key.txt') as f:
    openai_api_key = f.read()

# Create function for gradio chatbot
def gradio_chatbot(message: str, history: list) -> str:
    data_folder = "data"  # Path to the folder where PDFs are stored.
    pdf_files, pdf_names = read_pdf_files_from_folder(data_folder)

    # create vector database and index
    db = create_vectordb(pdf_files, pdf_names, openai_api_key)
    
    # retrieve 3 similar document chunks to the user query
    docs = db.similarity_search(message, k=3) 

    # add these document chunks to the system prompt
    #initialize system prompt to be added to the model
    system = {"role": "system", "content": system_prompt.format(pdf_extract=docs)}

    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})
    history_openai_format.append({"role": "user", "content": message})
    
    # Initialize the OpenAI client
    client = OpenAI(api_key=openai_api_key)

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[system] + history_openai_format,
        max_tokens=200,
        temperature=0,
        frequency_penalty=0,
        stream=True,
    )
    partial_message = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            partial_message = partial_message + chunk.choices[0].delta.content
            yield partial_message
            
gr.ChatInterface(
    gradio_chatbot, 
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder="Ask me a question", container=False, scale=7),
    title="AMEX Q&A Bot",
    description="Ask our AMEX Bot any question!",
    theme="soft",
    examples=["Am I eligible for travel insurance if I've only bought a 1 way ticket?", 
              "What am I covered for?", 
              "Who can I call if my card gets lost?"],
    cache_examples=True,
    retry_btn=None,
    undo_btn="Delete Previous",
    clear_btn="Clear",
).launch()

#ISSUES:
# queries like tell me more or i don't understand is not applicable

# Install packages
import os
import sys

#########################################################################################################
# Function to add root project directory to sys.path to import modules from there
def setup_module_path():
    # Get the directory of the current script
    current_dir = os.path.dirname(__file__)
    
    # Get the parent directory (root project directory)
    root_dir = os.path.abspath(os.path.join(current_dir, '..'))
    
    # Add the root project directory to sys.path
    sys.path.insert(0, root_dir)

# Call the function to set up the module path
# setup_module_path()

##########################################################################################################
# Get all PDF file names
def read_pdf_files_from_folder(folder_path: str):
    pdf_files = []
    pdf_names = []
    
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            pdf_names.append(file.rstrip(".pdf"))
            pdf_files.append(os.path.join("data", file))
    return pdf_files, pdf_names

#read_pdf_files_from_folder("data")

###########################################################################################################
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
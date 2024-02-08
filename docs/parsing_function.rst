========================
Replace Parsing Function 
========================

Date: 8/2/24

Original parsing function was from: https://github.com/avrabyt/RAG-Chatbot and looked like this:

.. code-block:: python

    def parse_pdf(file: BytesIO, filename: str) -> tuple[List[str], str]:

        # Initialize the PDF reader for the provided file.
        pdf = PdfReader(file)
        output = []
        
        # Loop through all the pages in the PDF.
        for page in pdf.pages:
            # Extract the text from the page.
            text = page.extract_text()
            
            # re.sub is used to find and then replace certain parts of the text to clean it up
            # Replace word splits that are split by hyphens at the end of a line.\
            text = re.sub(r"(\w+)-\n(\w+)", r"\1\2", text)
            
            # Replace single newlines with spaces, but not those flanked by spaces.
            text = re.sub(r"(?<!\n\s)\n(?!\s\n)", " ", text.strip())
            
            # Consolidate multiple newlines to two newlines.
            text = re.sub(r"\n\s*\n", "\n\n", text)
            
            # Append the cleaned text to the output list.
            output.append(text)
        
        # Return the list of cleaned texts and the filename.
        return output, filename

Can see that the regex in the above code snippet is more general and can apply to more use cases but in my code
wanted to clean the pdfs specific to the AMEX ones I've uploaded in data so I changed the regex. 
See docs\\regex_basics.ipynb for my experimentation.
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader    
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

# . .\.venv\Scripts\activate
# streamlit run app.py

# Function to get the text from the pdfs
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Function to get the text chunks
def get_text_chuncks(text):
     text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
     )
     chunks = text_splitter.split_text(text)
     return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

#   Function to get the text chunks
def main():

    # Load the environment variables
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple pdfs", 
                       page_icon=":books:")

    # Set the title and the description
    st.header("Chat with multiple pdfs :books:")
    st.text_input("Ask for a legislation prediction:")

    # Sidebar
    with st.sidebar:
        # Set the title of the sidebar
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
             "Upload your pdfs and 'Pocess'", type="pdf", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing..."):
                # get the pdf text
                raw_text = get_pdf_text(pdf_docs)
                # st.write(raw_text)

                # get the text chunks
                text_chunks = get_text_chuncks(raw_text)

                # get the vector stored in the database
                vectorstored = get_vectorstore(text_chunks)

#   Run the main function
if __name__ == '__main__':
        main()

# . .\.venv\Scripts\activate
# streamlit run app.py 

import streamlit as st
from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template, sidebar_text
from langchain.llms import HuggingFaceHub

# extract text from PDF files
def get_pdf_text(pdf_paths):
    text = ""
    for pdf_path in pdf_paths:
        pdf_reader = PdfReader(pdf_path)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# split text into chunks
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

# create a vector store from text chunks
def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

# create a conversation chain
def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

# handle user input and generate a response
def handle_userinput(user_question):
    if st.session_state.conversation:
        response = st.session_state.conversation({'question': user_question})
        st.session_state.chat_history = response['chat_history']
        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.markdown(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
            else:
                st.markdown(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
    else:
        st.warning("Please process the documents first.")

# run the Streamlit app
def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with LegisBot")
    st.markdown(css, unsafe_allow_html=True)
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    st.markdown('''
    <div align="center">
        <h3>Concept Statement</h3>
        <p>This research examines how policies in the world powers affect AI strategies and self-regulation in leading tech companies (the Big Nine). It explores the potential for AI to help regulate itself, given its understanding of its own systems and potential general intelligence. The project aims to highlight the need for ethical AI policies and international cooperation for the benefit of humanity.</p>
    </div>
    ''', unsafe_allow_html=True)

    st.header("Ask LegisBot about Legislation")
    user_question = st.text_input("Ask LegisBot a question related to legislation:")
    if user_question:
        handle_userinput(user_question)
    with st.sidebar:
        st.markdown(sidebar_text, unsafe_allow_html=True)
        
        st.subheader("Upload your PDF")
        uploaded_files = st.file_uploader("Add your PDF files here", accept_multiple_files=True, type=["pdf"])

        st.subheader("Process Saved Documents")
        st.markdown("Press the button to process saved documentation related to legislation, including any uploaded PDFs.")

        if st.button("Process", key="process-button"):
            with st.spinner("Processing"):
                # Get list of PDF files from the dataPool directory
                data_pool_dir = "src/dataPool"
                pdf_paths = [os.path.join(data_pool_dir, f) for f in os.listdir(data_pool_dir) if f.endswith('.pdf')]
                
                # Add uploaded files to the list
                if uploaded_files:
                    uploaded_file_paths = []
                    for uploaded_file in uploaded_files:
                        # Save the uploaded files to a temporary location
                        with open(os.path.join(data_pool_dir, uploaded_file.name), "wb") as f:
                            f.write(uploaded_file.getbuffer())
                        uploaded_file_paths.append(os.path.join(data_pool_dir, uploaded_file.name))
                    pdf_paths.extend(uploaded_file_paths)
                
                if pdf_paths:
                    # get pdf text
                    raw_text = get_pdf_text(pdf_paths)
                    # get the text chunks
                    text_chunks = get_text_chunks(raw_text)
                    # create vector store
                    vectorstore = get_vectorstore(text_chunks)
                    # create conversation chain
                    st.session_state.conversation = get_conversation_chain(vectorstore)
                else:
                    st.warning("No PDF files found in the dataPool directory.")

if __name__ == '__main__':
    main()

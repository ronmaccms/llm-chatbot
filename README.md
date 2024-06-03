<!-- PROJECT STATUS -->
<div align="center">
  <h3>🚧 This project is currently under development 🚧</h3>
</div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="https://github.com/ronmaccms/llm-chatbot/blob/main/src/img/Innovation-Tournaments.jpg" alt="Logo" width="450">
  <h3 align="center">AI Governance Chatbot</h3>
  <p align="center" style="font-weight: bold;">
    A project to analyze and suggest AI governance strategies<br >
    <a href="LINK_TO_DEMO">View Demo</a>
    ·
    <a href="andres.roncal@students.iaac.net">Report Bug</a>
    ·
    <a href="andres.roncal@students.iaac.net">Request Feature</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->

## About The Project
![Project image](assets/img/project-img.png)

This project is developed under the course IAAC: AI 2023-24 at [IAAC](https://iaac.net/).

__Project Breakdown__

This project is a Streamlit application that allows users to interact with a llm to ask questions about multiple PDF documents. The application uses openai to analyze the text from the PDF documents and generate responses to the user's questions. There is some code to connect to huggingface if you like as well.

Here's how it works:

1. **PDF Text Extraction:** The application reads the text from the uploaded PDF documents.

2. **Text Chunking:** The text from the PDFs is split into manageable chunks.

3. **Vector Store Creation:** A vector store is created from the text chunks using OpenAI embeddings. The vector store is a data structure that allows efficient similarity search of vectors.

4. **Conversation Chain Creation:** A conversation chain is created, which is a sequence of interactions between the user and the LLM. The conversation chain uses the vector store for retrieval of relevant text chunks and a memory buffer to keep track of the conversation history.

5. **User Interaction:** The user can ask a question about the documents, and the application will display the response.

This project is an example of how language learning models can be used to analyze and interact with text data in a user-friendly way. It demonstrates the power of AI in understanding and generating human-like text, providing useful and relevant responses to user queries.

<!-- AI Policies and Regulatory Frameworks (Company1): -->

<!-- __Task:__ Develop a web scraping script to collect data on AI policies and regulatory frameworks.
__Implementation:__ Use the provided GitHub script skeleton to scrape relevant websites and databases.
__Outcome:__ Clean, structured dataset for AI policies and regulatory frameworks.

AI Policies and Regulatory Frameworks (Company2, Company3, ... , Company9):

__Task:__ Extend the Company1 data collection process to the other Big Nine companies.
__Implementation:__ Adapt the Company1 script for each new company’s data sources.
__Outcome:__ Clean datasets for each company.

Self-Policing Practices (Company1, Company2, ... , Company9):

__Task:__ Gather data on the self-policing practices of the Big Nine.
__Implementation:__ Identify and extract data from reliable sources.
__Outcome:__ Clean dataset for the self-policing practices. -->

## Getting Started

To get a local copy up and running, follow these steps:

1. **Clone the repository**
    ```
    git clone https://github.com/your_username_/Project-Name.git
    ```

2. **Navigate to the project directory**
    ```
    cd Project-Name
    ```

3. **Create a Python virtual environment**
    ```
    python -m venv .venv
    ```

4. **Activate the virtual environment**
    - On Windows, use:
        ```
        . .\.venv\Scripts\activate
        ```
    - On Unix or MacOS, use:
        ```
        source .venv/bin/activate
        ```

5. **Create a .env file**
    - In the project directory, create a new file named `.env`.
    - Open the `.env` file and add your OpenAI and Hugging Face API keys like this:
        ```
        OPENAI_API_KEY=your_openai_api_key
        HUGGINGFACE_API_TOKEN=your_huggingface_api_token
        ```
    - Save the `.env` file. **Do not** commit this file to your repository. It contains sensitive information.

6. **Install the required packages**
    ```
    pip install -r requirements.txt
    ```

7. **Run the Streamlit app**
    ```
    streamlit run app.py
    ```

### Deactivation

When you're done working, you can deactivate the virtual environment by running: crtl + c
<!-- PROJECT STATUS -->
<!-- <div align="center">
  <h3>🚧 This project is currently under development 🚧</h3>
</div> -->

<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="https://github.com/ronmaccms/llm-chatbot/blob/main/src/img/Innovation-Tournaments.jpg" alt="Logo" width="450">
  <h3 align="center">AI Governance Chatbot</h3>
  <p align="center" style="font-weight: bold;">
    A project to analyze and suggest AI governance strategies<br>
<!--     <a href="https://github.com/ronmaccms/llm-chatbot/blob/main/src/img/legisbot-gettingstarted.mp4">View Demo</a>
    ·
    <a href="mailto:andres.roncal@students.iaac.net">Report Bug</a>
    ·
    <a href="mailto:andres.roncal@students.iaac.net">Request Feature</a> -->
  </p>
</div>

<!-- ABOUT THE PROJECT -->

## About The Project

Legisbot examines how policies in the world powers affect AI strategies and self-regulation in leading tech companies. It explores the potential for AI to help regulate itself, given its understanding of its own systems and potential general intelligence. The project aims to highlight the need for ethical AI policies and international cooperation for the benefit of humanity.

### Project Breakdown

This code is for a Streamlit application that allows users to upload PDF documents and use that text to answer questions related to AI legislation. The application uses OpenAI and generates responses to the user questions based on the text from the uploaded PDFs.

## Getting Started

To get a local copy up and running, follow these steps:

1. **Clone the repository**
    ```sh
    git clone https://github.com/your_username_/Project-Name.git
    ```

2. **Navigate to the project directory**
    ```sh
    cd Project-Name
    ```

3. **Activate the virtual environment**
    - On Windows, use:
        ```sh
        . .\.venv\Scripts\activate
        ```

4. **Add your Keys .env file**
    - Open the `.env` file and add your OpenAI and Hugging Face API keys like this:
        ```sh
        OPENAI_API_KEY=your_openai_api_key
        ```
    - Save the `.env` file. **Do not** commit this file to your repository. It contains sensitive information.

5. **Run the Streamlit app**
    ```sh
    streamlit run app.py
    ```

### Deactivation

When you're done working, you can deactivate the virtual environment by running:
```sh
ctrl + c

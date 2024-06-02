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
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#challenges">Challenges</a></li>
    <li><a href="#future-work">Future Work</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#team">Team</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>
<!-- ABOUT THE PROJECT -->

## About The Project
![Project image](assets/img/project-img.png)

This project is developed under the course IAAC: AI 2023-24 at [IAAC](https://iaac.net/).

__Project Breakdown__

__Data Collection:__ Gather data on AI policies, regulatory frameworks, and self-policing practices of the Big Nine tech companies in the United States and China.

__Model Training:__ Use the collected data to train the ML model to analyze the geopolitical and ethical implications of AI governance.

__Implementation:__ Deploy the trained model to suggest predictions or legislation for self-policing and to guide legislators.

__Data Collection Plan__

__We will focus on collecting data for the Big Nine tech companies, starting with Company1. The project is divided into three data sets, each assigned to a team member.__

AI Policies and Regulatory Frameworks (Company1):

__Task:__ Develop a web scraping script to collect data on AI policies and regulatory frameworks.
__Implementation:__ Use the provided GitHub script skeleton to scrape relevant websites and databases.
__Outcome:__ Clean, structured dataset for AI policies and regulatory frameworks.

AI Policies and Regulatory Frameworks (Company2, Company3, ... , Company9):

__Task:__ Extend the Company1 data collection process to the other Big Nine companies.
__Implementation:__ Adapt the Company1 script for each new company’s data sources.
__Outcome:__ Clean datasets for each company.

Self-Policing Practices (Company1, Company2, ... , Company9):

__Task:__ Gather data on the self-policing practices of the Big Nine.
__Implementation:__ Identify and extract data from reliable sources.
__Outcome:__ Clean dataset for the self-policing practices.



## Getting Started

To get a local copy up and running, follow these steps:

### Prerequisites

This project uses a Python virtual environment for managing dependencies. Make sure you have Python installed on your machine. You can download Python [here](https://www.python.org/downloads/).

### Installation

<h2>Getting Started</h2>

<p>To get a local copy up and running, follow these steps:</p>

<h3>Prerequisites</h3>

<p>This project uses a Python virtual environment for managing dependencies. Make sure you have Python installed on your machine. You can download Python <a href="https://www.python.org/downloads/">here</a>.</p>

<ol>
  <li>Clone the repository
    <pre><code>git clone https://github.com/your_username_/Project-Name.git</code></pre>
  </li>
  <li>Navigate to the project directory
    <pre><code>cd Project-Name</code></pre>
  </li>
  <li>Create a Python virtual environment
    <pre><code>python -m venv .venv</code></pre>
  </li>
  <li>Activate the virtual environment
    <ul>
      <li>On Windows, use:
        <pre><code>. .\.venv\Scripts\activate</code></pre>
      </li>
      <li>On Unix or MacOS, use:
        <pre><code>source .venv/bin/activate</code></pre>
      </li>
    </ul>
  </li>
  <li>Install the required packages
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
</ol>

<h3>Deactivation</h3>

<p>When you're done working, you can deactivate the virtual environment by running:</p>

<pre><code>deactivate</code></pre>
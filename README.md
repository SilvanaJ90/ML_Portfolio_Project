# Agent for Automatic SQL Analysis from Natural Language

**Agent for Automatic SQL Analysis from Natural Language** is an agent that extracts information from a SQL database, allowing users to make queries in natural language. The agent interprets these natural language queries and translates them into SQL format. The SQL engine then executes the query and returns the results to the LLM, which will present this information back to the user in natural language.

## Table of Contents

- [General project requirements](https://github.com/SilvanaJ90/ML-Portfolio?tab=readme-ov-file#general-project-requirements)
- [General functionalities](https://github.com/SilvanaJ90/ML-Portfolio?tab=readme-ov-file#general-functionalities)
- [AgentSQL](https://github.com/SilvanaJ90/ML-Portfolio?tab=readme-ov-file#chatbot---eleganceai)
- [How to Start It](https://github.com/SilvanaJ90/ML-Portfolio?tab=readme-ov-file#how-to-start-it)
- [Languages and Tools](https://github.com/SilvanaJ90/ML-Portfolio?tab=readme-ov-file#languages-and-tools)
- [Authors](https://github.com/SilvanaJ90/ML-Portfolio?tab=readme-ov-file#authors)

### General project requirements
EleganceAI is built on a robust RAG system, leveraging key technologies:

- LLM (Large Language Models) to provide consistent, automated responses to customer inquiries.
- NLP (Natural Language Processing) to understand customer context and generate personalized recommendations.
- Database and API integration to manage backend tasks like quotes, payments, and shipment tracking.

### General functionalities

The development of EleganceAI is structured into several key stages, each focusing on different aspects of the project:

- Backend Development
    Creation and connection of databases.
    Development of APIs, ensuring smooth integration with the e-commerce platform.

- RAG System Development
    Applying machine learning techniques to analyze customer preferences.
    Predicting products of interest, focusing on web integration to display real-time, dynamic recommendations.

### RAG System with LangChain Framework

![This is an image](https://github.com/SilvanaJ90/ML-Portfolio/blob/main/img/rag.png)

RAG System Architecture

| Components     | File | Description |
| -------------- | ------- | ----------- |
|Model I/O |[llm.py](https://github.com/SilvanaJ90/ML-Portfolio/blob/main/elegance/myapp/chatbot/llm.py)|The Model I/O focuses on basic inputs and outputs of the LLM, in this project the Google AI LLM  | 
|Data connectors|[vector_db.py](https://github.com/SilvanaJ90/ML-Portfolio/blob/main/elegance/myapp/chatbot/vector_db.py)| Data connector focuses on connecting an LLM to a data source such as your own documents or a vector store|
|Chains|[chain.py](https://github.com/SilvanaJ90/ML-Portfolio/blob/main/elegance/myapp/chatbot/chain.py) | Chains allow the output of one model to be linked as the input for another model call |
|Memory|[memory.py](https://github.com/SilvanaJ90/ML-Portfolio/blob/main/elegance/myapp/chatbot/memory.py)  | Memory allows your models to retain the historical context of previous interactions |
|Agent|[qa_bot.py](https://github.com/SilvanaJ90/ML-Portfolio/blob/main/elegance/myapp/chatbot/qa_bot.py) | Uses data connectors, data models, chains, memory, and provides a response to the user |

### AgentSQL

EleganceAI offers a chatbot that provides a personalized experience for Accesorios Elegance customers,
advising users on product choices and assisting with tasks like quotes and payments.

https://github.com/user-attachments/assets/ecd1033d-d9c2-4c7b-87b4-0359d30bfda1

### How to Start It

- Clone the project
```git clone   https://github.com/SilvanaJ90/ML-Portfolio.git ```
- Create a Google AI API key and save it in a .env file
```GOOGLE_API_KEY=your_api_key ```
- Install the required dependencies using the following command
``` pip install -r requirements.txt ```
- Navigate to the repository and then to the project
```cd elegance```
 - While inside the elegance project directory, run the server
  ```python3 manage.py runserver ```



### Languages and Tools
<h3 align="left">Backend:</h3>
<p align="left"> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/> </a> </p>

<h3 align="left">Database:</h3>
<p align="left"><a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"/> </a>

<h3 align="left">ML/AI:</h3>
 <p align="left"><a href="https://www.langchain.com/" target="_blank" rel="noreferrer"> <img src="https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white"/> </a>
  <a href="https://gemini.google.com" target="_blank" rel="noreferrer"> <img src="https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white"/> </a>
 <a href="https://huggingface.co/" target="_blank" rel="noreferrer"> <img src="https://img.shields.io/badge/-HuggingFace-FDEE21?style=for-the-badge&logo=HuggingFace&logoColor=black"/> </a></p>

## Authors
Silvana Jaramillo
<p><a href="https://linkedin.com/in/silvana-jaramillo" target="blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /> </a></p>
Alejandro Caballero
<p><a href="https://www.linkedin.com/in/alejandro-caballero-granado" target="blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /> </a></p>



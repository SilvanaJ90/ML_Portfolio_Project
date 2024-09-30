# Agent for Automatic SQL Analysis from Natural Language

**Agent for Automatic SQL Analysis from Natural Language** is an agent that extracts information from a SQL database, allowing users to make queries in natural language. The agent interprets these natural language queries and translates them into SQL format. The SQL engine then executes the query and returns the results to the LLM, which will present this information back to the user in natural language.

## Table of Contents

- [General project requirements](https://github.com/SilvanaJ90/ml_portfolio_project/tree/main?tab=readme-ov-file#general-project-requirements)
- [General functionalities](https://github.com/SilvanaJ90/ml_portfolio_project/tree/main?tab=readme-ov-file#general-functionalities)
- [AgentSQL](https://github.com/SilvanaJ90/ml_portfolio_project/tree/main?tab=readme-ov-file#agentsql)
- [How to Start It](https://github.com/SilvanaJ90/ml_portfolio_project/tree/main?tab=readme-ov-file#how-to-start-it)
- [Languages and Tools](https://github.com/SilvanaJ90/ml_portfolio_project/tree/main?tab=readme-ov-file#languages-and-tools)
- [Authors](https://github.com/SilvanaJ90/ml_portfolio_project/tree/main?tab=readme-ov-file#author)

### General Project Requirements

- **Python Version**: Ensure Python 3.x is installed.
- **Dependencies**: Required Python libraries must be installed (listed in `requirements.txt`).
- **PostgreSQL**: A PostgreSQL database server must be set up and accessible.
- **Google AI API Key**: A valid API key must be created and stored in a `.env` file.
- **Streamlit**: Streamlit should be installed to run the web application interface.
- **Data Files**: CSV files to be processed and inserted into the database should be available in the specified directory.

### General Functionalities

- **Data Processing**: The application can read, process, and clean data from CSV files.
- **Database Management**: read operations on a PostgreSQL database.
- **User Interface**: A web-based interface built with Streamlit for user interaction.
- **Natural Language Queries**: Users can interact with the database using natural language queries, which are translated into SQL queries.
- **Testing**: Ability to run test cases to ensure the application's functionality and reliability.


### AgentSQL

![This is an image](https://github.com/SilvanaJ90/ml_portfolio_project/blob/main/img/img.png)


video

### How to Start It

| Step                       | Command                                    | Description                                                             |
|----------------------------|--------------------------------------------|-------------------------------------------------------------------------|
| **Clone the project**       | `git clone https://github.com/SilvanaJ90/ml_portfolio_project.git` | Clone the project repository to your local machine.                    |
| **Create Google AI API key**| `GOOGLE_API_KEY=your_api_key`              | Create a Google AI API key and save it in a `.env` file.                |
| **Install dependencies**    | `pip install -r requirements.txt`          | Install all required dependencies for the project.                      |
| **Create the database and user** | `models/setup_postgres_dev.sql`      | Create the project's PostgreSQL database and user by running this SQL script. |
| **Run models.py**           | `models/models.py`                         | Execute the script to create the database tables.                       |
| **Data processing**         | `data_preprocessing.py`                    | Process the CSV file and prepare it for database insertion.             |
| **Insert data into the database** | `data/insert_data.py`               | Insert the processed CSV data into the database tables.                 |
| **Run the SQL agent**       | `streamlit run app.py`                     | Run the app with Streamlit, which allows users to query the database through an SQL agent. |
| **Run tests (optional)**    | `streamlit run tests.py`                   | For testing purposes, execute the test cases by running the tests file with Streamlit. |




### Languages and Tools
<p align="left">
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/> </a>
<a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"/> </a>
<a href="https://www.langchain.com/" target="_blank" rel="noreferrer"> <img src="https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white"/> </a>
<a href="https://gemini.google.com" target="_blank" rel="noreferrer"> <img src="https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white"/> </a>
<a https://streamlit.io/" target="_blank" rel="noreferrer"> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white"/> </a>
<a https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white"/> </a>
    
</p>

## Author
Silvana Jaramillo
<p><a href="https://linkedin.com/in/silvana-jaramillo" target="blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /> </a></p>

import streamlit as st
import os
from sqlalchemy import create_engine
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain.schema import HumanMessage
import google.generativeai as genai

# Configure Google Generative AI
API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=API_KEY)


def get_sql_agent():
    """ Function to create the connection and the agent """
    DATABASE_URL = (
        f"postgresql://{os.getenv('POSTGRES_USER')}:"
        f"{os.getenv('POSTGRES_PASSWORD')}@"
        f"{os.getenv('POSTGRES_HOST')}:"
        f"{os.getenv('POSTGRES_PORT')}/"
        f"{os.getenv('POSTGRES_DB')}"
    )

    # Create the SQLAlchemy engine
    engine = create_engine(DATABASE_URL)

    # Create the database instance
    db = SQLDatabase(engine)

    # Instantiate the Google Generative AI model
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash", google_api_key=API_KEY)

    # Create the SQL agent
    return create_sql_agent(llm, db=db, verbose=True)


st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #262730;
        }

        [data-testid="stSidebar"] .css-1d391kg {
            color: white;
        }

        }
    </style>
""", unsafe_allow_html=True)

# Application Title
st.title("Agent SQL")

# Create a container for the chat
chat_box = st.empty()
chat_history = []

# Input field for the question
question = st.text_input("Escribe tu pregunta...")

if st.button("Enviar"):
    if question.strip() == "":
        st.warning("Por favor, ingresa una pregunta.")
    else:
        chat_history.append(f"🧑‍💻: {question}")

        # Get the SQL agent
        agent = get_sql_agent()

        # Create the user message
        human_message = HumanMessage(content=question)

        # Invoke the agent with the message
        result = agent.invoke([human_message])

        # Extract the response from the result
        response = result.get(
            'output', 'Lo siento, no pude encontrar la respuesta.')
        chat_history.append(f":robot_face: {response}")

        # Display the chat history
        chat_box.text('\n'.join(chat_history))

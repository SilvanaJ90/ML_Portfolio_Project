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
    """Function to create the connection and the agent."""
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
        model="gemini-1.5-flash", google_api_key=API_KEY
    )

    # Create the SQL agent
    return create_sql_agent(llm, db=db, verbose=True)


# Streamlit app styling
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #262730;
        }
        [data-testid="stSidebar"] .css-1d391kg {
            color: white;
        }
        .st-chat-message {
            border: 1px solid #ccc;
            border-radius: 10px;
            padding: 10px;
            margin: 5px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Application Title
st.title("SQL Agent")

# Initialize chat history in session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Escribe tu pregunta..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": f" {prompt}"})

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(f" {prompt}")

    # Get the SQL agent
    agent = get_sql_agent()

    # Create the user message
    human_message = HumanMessage(content=prompt)

    # Invoke the agent with the message
    result = agent.invoke([human_message])

    # Extract the response from the result
    response = result.get(
        'output', 'Lo siento, no pude encontrar la respuesta.')

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(f"{response}")

    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": f" {response}"})

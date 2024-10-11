import os
import tensorflow as tf
from tensorflow import keras
import streamlit as st
from sqlalchemy import create_engine
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain.schema import HumanMessage
from transformers import AutoTokenizer  # Asegúrate de que esta línea coincide con tu tokenizer

# Cargar el modelo y el tokenizer
def load_model():
    """Función para cargar el modelo SQL"""
    model = keras.models.load_model('model_sql.h5')
    return model

def load_tokenizer():
    """Función para cargar el tokenizer"""
    tokenizer = AutoTokenizer.from_pretrained('ruta/al/modelo')  # Cambia 'ruta/al/modelo' al directorio de tu tokenizer
    return tokenizer

def generate_sql(question, model, tokenizer):
    """Función para generar SQL a partir de una pregunta usando el modelo cargado."""
    # Tokenización y generación del SQL
    inputs = tokenizer("translate English to SQL: " + question, return_tensors="tf", max_length=512, truncation=True, padding='max_length')
    outputs = model.generate(inputs['input_ids'], max_length=150)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def get_sql_agent(tokenizer):
    """Función para crear la conexión a la base de datos."""
    DATABASE_URL = (
        f"postgresql://{os.getenv('POSTGRES_USER')}:"
        f"{os.getenv('POSTGRES_PASSWORD')}@"
        f"{os.getenv('POSTGRES_HOST')}:"
        f"{os.getenv('POSTGRES_PORT')}/"
        f"{os.getenv('POSTGRES_DB')}"
    )

    # Crear el motor SQLAlchemy
    engine = create_engine(DATABASE_URL)

    # Crear la instancia de la base de datos
    db = SQLDatabase(engine)

    # Cargar el modelo de generación SQL
    sql_model = load_model()

    # Create the SQL agent
    return create_sql_agent(db=db, verbose=True)

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

# Cargar modelo y tokenizer al inicio
model = load_model()
tokenizer = load_tokenizer()

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
    agent = get_sql_agent(tokenizer)

    # Generar la consulta SQL usando el modelo cargado
    generated_sql = generate_sql(prompt, model, tokenizer)

    # Muestra la consulta generada
    response = f"Consulta SQL generada: {generated_sql}"

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(f"{response}")

    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": f" {response}"}
    )

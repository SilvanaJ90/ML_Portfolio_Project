import pandas as pd
from sqlalchemy import create_engine, text
import os
import streamlit as st

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

# Get environment variables
DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

# Create the database engine
engine = create_engine(DATABASE_URL)

# Definition of test cases
test_cases = {
    "SELECT count(*) FROM donantes WHERE Activo = 'SI';": {
        "question": "¿Cuántos donantes están activos?",
        "expected": 400,
    },
    "SELECT count(*) FROM donantes WHERE Activo = 'NO';": {
        "question": "¿Cuántos donantes están inactivos?",
        "expected": 199,  # Ajusta este valor según tus datos
    },
}


def run_tests():
    """ Function to run the tests """
    results = []

    for query, test in test_cases.items():
        with engine.connect() as connection:
            # Use text() to wrap the SQL query
            actual_count = connection.execute(text(query)).scalar()

        # Compare the expected value with the actual result
        is_correct = actual_count == test["expected"]
        results.append({
            "query": query,
            "question": test["question"],
            "expected": test["expected"],
            "actual": actual_count,
            "is_correct": is_correct,
        })

    return results


st.title("Resultados de la prueba de consulta SQL")


if st.button("Ejecutar Test"):
    results = run_tests()

    # Display the results in a table
    results_df = pd.DataFrame(results)
    st.table(results_df)

    correct_count = sum(result['is_correct'] for result in results)
    st.success(f"Pruebas correctas: {correct_count} de {len(results)}")

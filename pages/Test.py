import pandas as pd
from sqlalchemy import create_engine, text
import os
import streamlit as st

# Style for the interface
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #262730;
        }

        [data-testid="stSidebar"] .css-1d391kg {
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Get environment variables for database connection
DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

# Create the database engine
engine = create_engine(DATABASE_URL)

# Input interface for test cases
st.title("Editar casos de prueba SQL")

# Input for the SQL query
query = st.text_area("Insertar la consulta SQL", "SELECT SUM(importe) FROM donantes WHERE nro_cuenta = 402.101;")

# Input for the associated question
question = st.text_input("Insertar la pregunta", "What is the total amount of donations for account 402.101?")

# Input for the expected value
expected = st.number_input("Insertar el valor esperado", value=0.0, step=0.01, format="%.2f")

# Save the test case provided by the user
test_cases = {
    query: {
        "question": question,
        "expected": expected,
    }
}

def run_tests():
    """ Function to execute the tests """
    results = []
    tolerance = 0.01  # Define a margin of error for float comparison
    
    for query, test in test_cases.items():
        with engine.connect() as connection:
            # Execute the SQL query and get the result
            actual_count = connection.execute(text(query)).scalar()
        
        # Convert actual_count to float for comparison
        actual_count_float = float(actual_count)

        # Compare the expected value with the actual result (considering a margin for floats)
        is_correct = abs(actual_count_float - test["expected"]) < tolerance
        
        results.append({
            "query": query,
            "question": test["question"],
            "expected": test["expected"],
            "actual": actual_count_float,  # Show the converted value
            "is_correct": is_correct,
        })

    return results

# Button to run the test
if st.button("Ejecutar Test"):
    results = run_tests()

    # Display the results in a table
    results_df = pd.DataFrame(results)
    st.table(results_df)

    correct_count = sum(result['is_correct'] for result in results)
    st.success(f"Correct tests: {correct_count} out of {len(results)}")

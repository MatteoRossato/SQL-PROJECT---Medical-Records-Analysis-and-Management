import sqlite3
import pandas as pd

# DB Connection
def execute_query(query):
    conn = sqlite3.connect("medical_records.db")
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Execute some queries
queries = {
    "Total Patients": "SELECT COUNT(*) AS total_patients FROM Patients;",
    "Most Common Diagnoses": """
        SELECT diagnosis, COUNT(*) AS occurrences 
        FROM Diagnoses 
        GROUP BY diagnosis 
        ORDER BY occurrences DESC;
    """,
    "Average Age by Diagnosis": """
        SELECT d.diagnosis, AVG(p.age) AS avg_age
        FROM Diagnoses d
        JOIN Patients p ON d.patient_id = p.patient_id
        GROUP BY d.diagnosis;
    """
}

# Stamp Results
for title, query in queries.items():
    print(f"\n{title}")
    print(execute_query(query))


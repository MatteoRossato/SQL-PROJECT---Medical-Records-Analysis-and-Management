import sqlite3
import pandas as pd

# DB Connection
conn = sqlite3.connect("medical_records.db")
cursor = conn.cursor()

# Table Creation
with open("sql/schema.sql", "r") as f:
    cursor.executescript(f.read())

# Patients Upload
df = pd.read_csv("data/patients.csv")
for _, row in df.iterrows():
    cursor.execute("INSERT INTO Patients (name, age, gender, admission_date) VALUES (?, ?, ?, ?)", 
                   (row["name"], row["age"], row["gender"], row["admission_date"]))

# "Addition of fictitious diagnoses"
diagnoses = [
    (1, "Diabete", 3, "2024-03-02"),
    (1, "Ipertensione", 2, "2024-03-03"),
    (2, "Covid-19", 4, "2024-03-06"),
    (3, "Asma", 2, "2024-03-11")
]

cursor.executemany("INSERT INTO Diagnoses (patient_id, diagnosis, severity, diagnosis_date) VALUES (?, ?, ?, ?)", diagnoses)

# Save
conn.commit()
conn.close()


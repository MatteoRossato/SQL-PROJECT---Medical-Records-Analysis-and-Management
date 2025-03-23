from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Connessione al database
def query_db(query):
    conn = sqlite3.connect("medical_records.db")
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route("/patients", methods=["GET"])
def get_patients():
    data = query_db("SELECT * FROM Patients")
    return jsonify(data)

@app.route("/diagnoses", methods=["GET"])
def get_diagnoses():
    data = query_db("SELECT * FROM Diagnoses")
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)


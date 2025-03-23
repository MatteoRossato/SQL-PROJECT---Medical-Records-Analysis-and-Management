-- DB creation
DROP TABLE IF EXISTS Patients;
DROP TABLE IF EXISTS Diagnoses;

CREATE TABLE Patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT CHECK (gender IN ('M', 'F')),
    admission_date DATE
);

CREATE TABLE Diagnoses (
    diagnosis_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    diagnosis TEXT NOT NULL,
    severity INTEGER CHECK (severity BETWEEN 1 AND 5),
    diagnosis_date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);


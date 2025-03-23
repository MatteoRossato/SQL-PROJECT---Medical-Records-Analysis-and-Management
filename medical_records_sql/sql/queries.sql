-- Patients Count
SELECT COUNT(*) AS total_patients FROM Patients;

-- Common diagnosis
SELECT diagnosis, COUNT(*) AS occurrences 
FROM Diagnoses 
GROUP BY diagnosis 
ORDER BY occurrences DESC;

-- Average age 
SELECT d.diagnosis, AVG(p.age) AS avg_age
FROM Diagnoses d
JOIN Patients p ON d.patient_id = p.patient_id
GROUP BY d.diagnosis;

-- Patients with multiple diagnosis
SELECT p.name, COUNT(d.diagnosis) AS num_diagnoses
FROM Patients p
JOIN Diagnoses d ON p.patient_id = d.patient_id
GROUP BY p.name
HAVING num_diagnoses > 1;


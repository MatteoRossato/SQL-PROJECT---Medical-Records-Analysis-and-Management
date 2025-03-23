# SQL-PROJECT---Medical_Records_Analysis_and_Management

## **🩺 Medical Records SQL**  
A **SQL database** for managing medical records and performing data analysis. This project uses **SQLite** to store patient and diagnosis data, allowing advanced analysis through **SQL queries** and **Python scripts**. It also includes a **Flask API** for structured data access.  

---

## **📌 Key Features**  
✅ **SQL Database** with relational tables for patients and diagnoses  
✅ **Advanced SQL queries** for medical data analysis  
✅ **Automatic database population** with sample data  
✅ **Data analysis with Python and Pandas**  
✅ **REST API with Flask** for easy data access  

---

## **📁 Project Structure**
```bash
📂 medical_records_sql  
 ┣ 📂 data  
 ┃ ┣ patients.csv         # Sample dataset  
 ┣ 📂 sql  
 ┃ ┣ schema.sql           # Database creation script  
 ┃ ┣ queries.sql          # SQL queries for analysis  
 ┣ 📂 src  
 ┃ ┣ db.py                # Database connection management  
 ┃ ┣ populate_db.py       # Script to populate the database  
 ┃ ┣ analytics.py         # SQL query execution  
 ┣ app.py                 # Flask API for data access  
 ┣ requirements.txt        # Project dependencies  
 ┣ README.md              # Documentation  
```

---

## **🔧 Installation**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/medical_records_sql.git
cd medical_records_sql
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Create and Populate the Database**
```bash
python src/populate_db.py
```

### **4️⃣ Run SQL Data Analysis**
```bash
python src/analytics.py
```

### **5️⃣ Start the API**
```bash
python app.py
```
The API will be available at `http://127.0.0.1:5000/`

---

## **📊 Database Structure**
The database contains two main tables:  

### **👨‍⚕️ "Patients" Table**
| Column         | Type     | Description |
|---------------|---------|-------------|
| patient_id    | INTEGER | Unique patient ID (PK) |
| name          | TEXT    | Patient's full name |
| age           | INTEGER | Patient's age |
| gender        | TEXT    | Gender (M/F) |
| admission_date | DATE   | Hospital admission date |

### **📝 "Diagnoses" Table**
| Column         | Type     | Description |
|---------------|---------|-------------|
| diagnosis_id  | INTEGER | Unique diagnosis ID (PK) |
| patient_id    | INTEGER | Patient ID (FK) |
| diagnosis     | TEXT    | Diagnosis name |
| severity      | INTEGER | Severity level (1 = mild, 5 = severe) |
| diagnosis_date | DATE   | Date of diagnosis |

---

## **📑 SQL Query Examples**
Some of the SQL queries used in the project:  

### 🔹 **Total Number of Patients**
```sql
SELECT COUNT(*) AS total_patients FROM Patients;
```

### 🔹 **Most Common Diagnoses**
```sql
SELECT diagnosis, COUNT(*) AS occurrences 
FROM Diagnoses 
GROUP BY diagnosis 
ORDER BY occurrences DESC;
```

### 🔹 **Average Age of Patients by Diagnosis**
```sql
SELECT d.diagnosis, AVG(p.age) AS avg_age
FROM Diagnoses d
JOIN Patients p ON d.patient_id = p.patient_id
GROUP BY d.diagnosis;
```

### 🔹 **Patients with Multiple Diagnoses**
```sql
SELECT p.name, COUNT(d.diagnosis) AS num_diagnoses
FROM Patients p
JOIN Diagnoses d ON p.patient_id = d.patient_id
GROUP BY p.name
HAVING num_diagnoses > 1;
```

---

## **🌐 REST API with Flask**
The API provides access to stored medical data.  

### **🟢 Available Endpoints**
| Method | Endpoint   | Description |
|--------|-----------|-------------|
| GET    | `/patients`  | Returns a list of all patients |
| GET    | `/diagnoses` | Returns a list of all diagnoses |

### **🛠️ Example Requests**
📌 **Get Patient List**  
```bash
curl -X GET "http://127.0.0.1:5000/patients"
```

📌 **Get Diagnoses**  
```bash
curl -X GET "http://127.0.0.1:5000/diagnoses"
```

---

## **📌 API Response Example**
Request:  
```bash
curl -X GET "http://127.0.0.1:5000/patients"
```
JSON Response:
```json
[
  {
    "patient_id": 1,
    "name": "Mario Rossi",
    "age": 55,
    "gender": "M",
    "admission_date": "2024-03-01"
  },
  {
    "patient_id": 2,
    "name": "Anna Bianchi",
    "age": 45,
    "gender": "F",
    "admission_date": "2024-03-05"
  }
]
```

---

## **📌 Contributing**
If you want to contribute:  
1. **Fork** the repository  
2. Create a **new branch**  
3. Add your changes and **commit**  
4. Submit a **pull request**  

---

## **📜 License**
This project is released under the **MIT License**.

---

## **📢 Contact**
📧 Email: [your@email.com](matteorossato95@gmail.com)  

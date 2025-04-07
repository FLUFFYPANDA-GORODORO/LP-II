import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Database Connection
def connect_db():
    conn = sqlite3.connect("medical_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS diagnoses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symptoms TEXT,
            diagnosis TEXT
        )
    """)
    conn.commit()
    return conn

db_conn = connect_db()


def save_diagnosis(symptoms, diagnosis):
    cursor = db_conn.cursor()
    cursor.execute("INSERT INTO diagnoses (symptoms, diagnosis) VALUES (?, ?)", (symptoms, diagnosis))
    db_conn.commit()

# Rule-based Diagnosis
symptom_diagnosis_map = {
    ("fever", "cough"): "Possible conditions: Flu, COVID-19, Bronchitis",
    ("headache", "fatigue"): "Possible conditions: Migraine, Anemia, Stress",
    ("chest pain", "shortness of breath"): "Possible conditions: Heart Disease, Anxiety Disorder",
    ("nausea", "sore throat"): "Possible conditions: Gastroenteritis, Strep Throat",
}

def diagnose():
    selected_symptoms = [symptom_var.get() for symptom_var in symptom_vars if symptom_var.get()]
    if not selected_symptoms:
        messagebox.showwarning("Warning", "Please select at least one symptom.")
        return
    
    diagnosis = "No matching condition found. Please consult a doctor."
    for symptoms, condition in symptom_diagnosis_map.items():
        if all(symptom in selected_symptoms for symptom in symptoms):
            diagnosis = condition
            break
    
    messagebox.showinfo("Diagnosis Result", diagnosis)
    save_diagnosis(", ".join(selected_symptoms), diagnosis)

# GUI Setup
root = tk.Tk()
root.title("Rule-Based Medical Diagnosis Expert System")
root.geometry("500x400")

# UI Components
tk.Label(root, text="Select Symptoms:").pack(pady=5)
symptom_list = ["fever", "cough", "headache", "fatigue", "chest pain", "nausea", "sore throat", "shortness of breath"]
symptom_vars = [tk.StringVar() for _ in symptom_list]

for i, symptom in enumerate(symptom_list):
    ttk.Checkbutton(root, text=symptom, variable=symptom_vars[i], onvalue=symptom, offvalue="").pack(anchor="w")

ttk.Button(root, text="Diagnose", command=diagnose).pack(pady=10)
root.mainloop()

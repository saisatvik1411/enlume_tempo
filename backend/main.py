# timesheet_backend/main.py
from fastapi import FastAPI, Depends
from pydantic import BaseModel
import psycopg2
import csv

app = FastAPI()

def get_db_connection():
    return psycopg2.connect(
        dbname="timesheet_db", user="admin", password="admin", host="postgres", port="5432"
    )

class TimeEntry(BaseModel):
    employee_id: str
    date: str
    hours_spent: float

@app.post("/log-time/")
def log_time(entry: TimeEntry):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO timesheets (employee_id, date, hours_spent) VALUES (%s, %s, %s)",
                   (entry.employee_id, entry.date, entry.hours_spent))
    conn.commit()
    conn.close()
    return {"message": "Time logged successfully"}

@app.get("/generate-report/{month}")
def generate_monthly_report(month: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM timesheets WHERE date LIKE %s", (month + '%',))
    records = cursor.fetchall()
    with open(f"/app/reports/timesheet_{month}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Employee ID", "Date", "Hours Spent"])
        writer.writerows(records)
    conn.close()
    return {"message": f"Report timesheet_{month}.csv generated."}
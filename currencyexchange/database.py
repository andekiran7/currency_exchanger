import sqlite3  # Add this line
from config import DATABASE_FILE

def setup_database():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS alerts (currency TEXT, threshold REAL)")
    conn.commit()
    conn.close()

def add_alert(currency, threshold):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alerts (currency, threshold) VALUES (?, ?)", (currency, threshold))
    conn.commit()
    conn.close()

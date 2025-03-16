# fetch_rates.py
import requests
import sqlite3
from config import API_URL, DATABASE_FILE

def fetch_exchange_rate(base_currency):
    response = requests.get(f"{API_URL}{base_currency}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def save_rates_to_db(base_currency, rates):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS rates (currency TEXT, rate REAL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")
    for currency, rate in rates.items():
        cursor.execute("INSERT INTO rates (currency, rate) VALUES (?, ?)", (currency, rate))
    conn.commit()
    conn.close()

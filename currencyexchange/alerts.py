import sqlite3  # Add this line
from config import DATABASE_FILE  # Add this line

def check_alerts():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    # Fetch all alerts from the database
    cursor.execute("SELECT currency, threshold FROM alerts")
    alerts = cursor.fetchall()

    # Fetch the latest exchange rates
    cursor.execute("SELECT currency, rate FROM rates ORDER BY timestamp DESC")
    latest_rates = {currency: rate for currency, rate in cursor.fetchall()}
    
    conn.close()

    # Check if any currency has reached the threshold
    for currency, threshold in alerts:
        if currency in latest_rates and latest_rates[currency] >= threshold:
            print(f"🔔 Alert! {currency} has reached {latest_rates[currency]}")


# main.py
import time
from fetch_rates import fetch_exchange_rate, save_rates_to_db
from database import setup_database, add_alert
from alerts import check_alerts

def main():
    setup_database()
    base_currency = "USD"
    while True:
        data = fetch_exchange_rate(base_currency)
        if data:
            save_rates_to_db(base_currency, data["rates"])
            check_alerts()
        time.sleep(60)  # Fetch rates every minute

if __name__ == "__main__":
    main()
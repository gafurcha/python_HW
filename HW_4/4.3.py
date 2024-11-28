import pandas as pd
import time
import requests
from datetime import datetime

currency_df = pd.DataFrame(columns=['Время', 'USD/EUR'])

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def fetch_currency_rate():
    try:
        response = requests.get(API_URL)

        if response.ok:
            data = response.json()
            usd_to_eur = data['rates']['EUR']
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            global currency_df
            new_row = pd.DataFrame({'Время': [current_time], 'USD/EUR': [usd_to_eur]})
            currency_df = pd.concat([currency_df, new_row], ignore_index=True)

            print(f"{current_time} - Курс USD к EUR: {usd_to_eur}")
        else:
            print(f"Ошибка при запросе данных: HTTP статус {response.status_code}")

    except requests.exceptions.RequestException as error:
        print(f"Ошибка соединения: {error}")


def main():
    interval = 1800  # Интервал обновления в секундах (30 минут)
    print("Программа запущена. Каждые 30 минут будет обновляться курс валют.")

    while True:
        fetch_currency_rate()
        time.sleep(interval)


if __name__ == "__main__":
    main()
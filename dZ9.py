#pip install requests beautifulsoup4

import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time



def create_database():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            date TEXT,
            time TEXT,
            temperature REAL
        )
    ''')

    conn.commit()
    conn.close()


def get_temperature(city):
    # Замените на актуальный URL для вашего города
    url = f'https://weather.com/ru-RU/weather/today/l/f3155899c90b24c622f264da14541544c8519a80d84ce07fe2b4529bd511e3bf{city}'
    response = requests.get(url)



    # Найдите нужный элемент на странице, который содержит температуру
    temperature_element = soup.find('span', class_='CurrentConditions--tempValue--3a50n')

    if temperature_element:
        temperature = temperature_element.text
        return float(temperature.replace('°', '').replace(',', '.'))
    else:
        print("Не удалось найти элемент с температурой.")
        return None


# Функция для обновления погоды
def update_weather(city):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()

    while True:
        temperature = get_temperature(city)

        if temperature is not None:
            now = datetime.now()
            date_str = now.strftime('%Y-%m-%d')
            time_str = now.strftime('%H:%M:%S')

            cursor.execute('''
                INSERT INTO weather (date, time, temperature)
                VALUES (?, ?, ?)
            ''', (date_str, time_str, temperature))

            conn.commit()
            print(f'Обновлено: {date_str} {time_str} - {temperature}°C')

        time.sleep(1800)  # Пауза на 30 минут


if __name__ == '__main__':
    create_database()
    city = 'Dnepropetrovsk'  # Замените на актуальный код города
    update_weather(city)
import requests
from bs4 import BeautifulSoup
import sqlite3
import logging
from datetime import datetime, timedelta

# Налаштування логування
logging.basicConfig(level=logging.INFO)


# Клас для збору даних з веб-сторінок
class WeatherScraper:
    def __init__(self, city):
        self.city = city
        self.base_url = f"https://www.gismeteo.ua/weather-dnipro-5077/"

    def fetch_weather_data(self, days=7):
        weather_data = []
        for i in range(days):
            date = (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d')
            response = requests.get(self.base_url)
            if response.status_code != 200:
                logging.error(f"Failed to fetch data for {date}. Status code: {response.status_code}")
                continue

            soup = BeautifulSoup(response.text, 'html.parser')

            # Припустимо, що дані про погоду мають певну структуру
            try:
                temperature = soup.find(class_='temp').text.strip()
                precipitation = 'Так' if 'опади' in soup.text else 'Ні'
                wind_speed = soup.find(class_='wind-speed').text.strip()
                wind_direction = soup.find(class_='wind-direction').text.strip()

                weather_data.append({
                    'date': date,
                    'temperature': temperature,
                    'precipitation': precipitation,
                    'wind_speed': wind_speed,
                    'wind_direction': wind_direction
                })
            except Exception as e:
                logging.error(f"Error parsing data for {date}: {e}")
        return weather_data


# Клас для запису даних у базу даних SQLite3
class WeatherDatabase:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS weather (
                    id INTEGER PRIMARY KEY,
                    date TEXT,
                    temperature TEXT,
                    precipitation TEXT,
                    wind_speed TEXT,
                    wind_direction TEXT
                )
            ''')

    def insert_weather_data(self, weather_data):
        with self.connection:
            self.connection.executemany('''
                INSERT INTO weather (date, temperature, precipitation, wind_speed, wind_direction)
                VALUES (:date, :temperature, :precipitation, :wind_speed, :wind_direction)
            ''', weather_data)

    def fetch_weather_by_date(self, date):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM weather WHERE date = ?', (date,))
        return cursor.fetchall()

    def fetch_weather_by_temperature_range(self, min_temp, max_temp):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM weather WHERE temperature BETWEEN ? AND ?', (min_temp, max_temp))
        return cursor.fetchall()


# Клас для зберігання даних про погоду
class DateWeather:
    def __init__(self, date, temperature, precipitation, wind_speed, wind_direction):
        self.date = date
        self.temperature = temperature
        self.precipitation = precipitation
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction

    def __str__(self):
        return (f"Дата: {self.date}, "
                f"Температура: {self.temperature}, "
                f"Опади: {self.precipitation}, "
                f"Швидкість вітру: {self.wind_speed}, "
                f"Напрямок вітру: {self.wind_direction}")


# Основна частина програми
if __name__ == "__main__":
    city = "Дніпро"
    scraper = WeatherScraper(city)
    weather_data = scraper.fetch_weather_data(days=7)

    db = WeatherDatabase('weather_data.db')
    db.insert_weather_data(weather_data)

    # Виведення даних з бази даних
    print("Дані про погоду за останні 7 днів:")
    for data in weather_data:
        weather_entry = DateWeather(**data)
        print(weather_entry)

    # Приклад вибірки даних за датою
    specific_date = (datetime.now()).strftime('%Y-%m-%d')
    print(f"\nДані погоди для {specific_date}:")
    results = db.fetch_weather_by_date(specific_date)
    for row in results:
        print(row)

    # Приклад
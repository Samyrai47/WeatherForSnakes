import requests
import os

class WeatherAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = 'https://api.openweathermap.org/data/2.5/weather'

    def get_weather_data(self, city: str) -> dict:
        params = {
            'q': city,
            'units': 'metric',
            'lang': 'ru',
            'appid': self.api_key
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f'Ошибка при запросе погоды: {e}')
            return {}
        except KeyError:
            print(f'Не удалось определить город: {city}')
            return {}

class WeatherReport(WeatherAPI):
    def display_weather(self, city: str) -> None:
        weather_data = self.get_weather_data(city)
        if weather_data:
            try:
                temperature = weather_data['main']['temp']
                temperature_feels = weather_data['main']['feels_like']
                wind_speed = weather_data['wind']['speed']
                cloud_cover = weather_data['weather'][0]['description']
                humidity = weather_data['main']['humidity']
                return (temperature, temperature_feels, wind_speed, cloud_cover, humidity)
            except KeyError:
                print(f'Не удалось получить данные о погоде для города: {city}')

if __name__ == "__main__":
    api_key = os.getenv('WEATHER_API_KEY')
    city = input('Введите город, в котором хотите узнать погоду: ')
    weather_report = WeatherReport(api_key)
    weather_report.display_weather(city)

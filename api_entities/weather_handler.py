import dotenv
from api.api import WeatherAPI


class WeatherHandler:
    PATH_TO_ENV = '../.env'

    def __init__(self):
        self.api_key = dotenv.get_key(WeatherHandler.PATH_TO_ENV, 'SECRET_KEY')
        self.api = WeatherAPI(self.api_key)

    def export_data(self, city):
        data = self.api.get_weather_data(city)
        return data

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


class WeatherData:
    def __init__(self, json_data):
        for key, value in dict(json_data['main']).items():
            try:
                self.__dict__[key] = value
            except:
                self.__dict__[key] = 'Значение не указано'

    def list_of_names(self):
        return self.__dict__.keys()

    def __getattr__(self, item):
        return self.__dict__[item]

    def __setattr__(self, key, value):
        self.__dict__[key] = value


handler = WeatherHandler()
data = WeatherData(handler.export_data('Москва'))
print(data.list_of_names())

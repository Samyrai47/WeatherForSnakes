from api_entities.weather_handler import WeatherHandler


class WeatherData:
    def __init__(self, json_data):
        for key, value in dict(json_data['main']).items():
            try:
                self.__dict__[key] = value
            except KeyError:
                self.__dict__[key] = None

        try:
            self.clouds = json_data['clouds']['all']
        except KeyError:
            self.clouds = None

        try:
            self.wind_speed = json_data['wind']['speed']
        except KeyError:
            self.wind_speed = None

    def list_of_names(self):
        return self.__dict__.keys()

    def __getattr__(self, item):
        return self.__dict__[item]

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __str__(self):
        return str(self.__dict__.items())


if __name__ == '__main__':
    handler = WeatherHandler()
    data = WeatherData(handler.export_data('Новосибирск'))
    print(data)

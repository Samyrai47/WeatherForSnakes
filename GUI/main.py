import sys
import datetime
import time

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QGridLayout
from PyQt6 import QtCore, QtGui, QtWidgets
import locale

from api_entities.weather_data import WeatherData
from api_entities.weather_handler import WeatherHandler

locale.setlocale(
    category=locale.LC_ALL,
    locale="Russian"  # Note: do not use "de_DE" as it doesn't work
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_window()
        self.init_tools()

        self.welcome_label = self.init_welcome_label()
        self.name_label = self.init_name_label()
        self.push_button = self.init_push_button()

        self.push_button.clicked.connect(self.show_my_window)

    def init_window(self):
        self.setWindowTitle("Weather For Snakes")
        self.setEnabled(True)
        self.setWindowTitle("WeatherForSnakes")
        self.setFixedSize(1280, 720)
        self.setWindowIcon(QtGui.QIcon('../images/snake.jpeg'))

    def init_tools(self):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(17, 52, 74))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        self.setPalette(palette)

    def init_welcome_label(self):
        welcome_label = QLabel("Добро пожаловать на сервис", self)
        welcome_label.setGeometry(0, 250, 1280, 200)
        welcome_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        welcome_label.setStyleSheet(
            # Шрифт
            'color: #fae1c2;'
            'font-family: Noto Serif;'
            'font-size: 26px;'
        )

        return welcome_label

    def init_name_label(self):
        name_label = QLabel("Weather For Snakes", self)
        name_label.setGeometry(0, 300, 1280, 400)
        name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        name_label.setStyleSheet(
            # Шрифт
            'color: #fae1c2;'
            'font-family: Noto Serif;'
            'font-size: 32px;'
        )
        return name_label

    def init_push_button(self):
        push_button = QPushButton("Продолжить", self)
        push_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        push_button.setGeometry(QtCore.QRect(350, 510, 600, 50))
        push_button.setStyleSheet(
            # Границы, цвет
            'background-color: #f9df76;'

            # Шрифт
            'color: #000000;'
            'font-family: Noto Serif;'
            'font-size: 24px;'
        )

        return push_button

    def show_my_window(self):
        self.ui = MyWindow()
        self.ui.show()
        self.hide()

    def show_my_window2(self):
        self.ui = MyWindow()
        self.ui.show()


class MyWindow(QMainWindow):
    def init_window(self):
        self.setWindowTitle("Weather For Snakes")
        self.setFixedSize(1280, 720)
        self.setWindowIcon(QtGui.QIcon('../images/snake.jpeg'))

    def init_tools(self):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(17, 52, 74))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        self.setPalette(palette)

    def init_background(self):
        logo = QtWidgets.QLabel(self)
        logo.setGeometry(250, 0, 700, 700)
        pixmap = QPixmap('../images/snake.jpeg')
        logo.setPixmap(pixmap)
        return logo

    def init_input_field(self):
        edit_text = QLineEdit("", self)
        edit_text.setGeometry(50, 170, 600, 50)
        edit_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        edit_text.setStyleSheet(
            # Границы, цвет
            'background-color: #000000;'

            # Шрифт
            'color: #fae1c2;'
            'font-family: Noto Serif;'
            'font-size: 24px;'
            'font-weight: bold;'
        )
        return edit_text

    def init_push_button(self):
        push_button = QtWidgets.QPushButton("Продолжить", self)
        push_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        push_button.setGeometry(QtCore.QRect(650, 170, 200, 50))
        push_button.setStyleSheet(
            # Границы, цвет
            'background-color: #f9df76;'

            # Шрифт
            'color: #000000;'
            'font-family: Noto Serif;'
            'font-size: 24px;'
        )
        return push_button

    def init_city_label(self):
        city_label = QtWidgets.QLabel("Введите город:", self)
        city_label.setGeometry(50, 110, 400, 30)
        city_label.setStyleSheet(
            # Шрифт
            'color: #fae1c2;'
            'font-family: Noto Serif;'
            'font-size: 26px;'
        )
        return city_label

    def init_progress_bar(self):
        progress_bar = QtWidgets.QProgressBar(self)
        progress_bar.hide()
        progress_bar.setGeometry(450, 450, 400, 30)
        progress_bar.setMaximum(100)
        progress_bar.setStyleSheet(
            # Шрифт
            'color: #ffffff;'
            'font-family: Noto Serif;'
            'font-size: 26px;'
        )
        return progress_bar

    def init_time_label(self):
        now = datetime.datetime.now()

        time_label = QtWidgets.QLabel("", self)
        time_label.setGeometry(50, 40, 300, 50)
        time_label.setStyleSheet(
            # Шрифт
            'color: #fae1c2;'
            'font-family: Noto Serif;'
            'font-size: 26px;'
        )

        time_label.setText(now.strftime("%a, %d %b, %H:%M"))
        return time_label

    def init_weather_image(self):
        weather_image = QtWidgets.QLabel(self)
        weather_image.hide()
        weather_image.setGeometry(0, 250, 1280, 600)
        return weather_image

    def init_get_weather_button(self):
        get_weather_button = QtWidgets.QPushButton(self)
        get_weather_button.hide()
        get_weather_button.setGeometry(50, 300, 1180, 370)
        get_weather_button.setEnabled(False)
        get_weather_button.setStyleSheet(
            'background-color: rgba(28,28,28,100);'
        )
        return get_weather_button

    def init_temp_label(self):
        temp_tabel = QtWidgets.QLabel("", self)
        temp_tabel.hide()
        temp_tabel.setGeometry(600, 425, 200, 100)
        temp_tabel.setStyleSheet(
            'color: #fae1c2;'
            'font-family: Noto Serif;'
            'font-size: 128px;'
        )
        return temp_tabel

    def init_temp_feels_label(self):
        temp_feels_label = QtWidgets.QLabel("", self)
        temp_feels_label.hide()
        temp_feels_label.setGeometry(500, 300, 400, 100)
        temp_feels_label.setStyleSheet(
            'color: #fae1c2;'
            'font-family: Noto Serif;'
            'font-size: 32px;'
        )
        return temp_feels_label

    def init_additional_info_label(self):
        additional_info_label = QtWidgets.QLabel("", self)
        additional_info_label.hide()
        additional_info_label.setGeometry(330, 550, 700, 100)
        additional_info_label.setStyleSheet(
            'color: #fae1c2;'
            'font-family: Noto Serif;'
            'font-size: 32px;'
        )
        return additional_info_label

    def init_error_message_label(self):
        error_message_label = QtWidgets.QLabel(self)
        error_message_label.setGeometry(600, 425, 200, 100)
        error_message_label.setStyleSheet(
            'color: #fae1c2;'
            'font-family: Noto Serif;'
            'font-size: 32px;'
        )
        return error_message_label

    def __init__(self):
        super().__init__()

        self.init_window()
        self.init_tools()

        self.handler = WeatherHandler()

        self.logo = self.init_background()
        self.city_label = self.init_city_label()
        self.time_label = self.init_time_label()
        self.weather_image = self.init_weather_image()
        self.temp_tabel = self.init_temp_label()
        self.temp_feels_label = self.init_temp_feels_label()
        self.additional_info_label = self.init_additional_info_label()
        self.error_message_label = self.init_error_message_label()

        self.edit_text = self.init_input_field()
        self.menu_button = self.init_get_weather_button()
        self.progress_bar = self.init_progress_bar()

        self.get_weather_response_button = self.init_push_button()
        self.get_weather_response_button.clicked.connect(self.button_clicked)

        layout = QGridLayout(self)
        layout.addWidget(self.temp_tabel)

    def button_clicked(self):
        self.menu_button.hide()
        self.weather_image.hide()
        self.temp_tabel.hide()
        self.temp_feels_label.hide()
        self.additional_info_label.hide()

        try:
            data = WeatherData(self.handler.export_data(self.edit_text.text()))
            self.start_progress()

            # Все значения здесь должны подставляться из API, пока просто тестовые данные стоят
            self.check_clouds(data.clouds)
            self.temp_tabel.setText(f'{data.temp}')
            self.temp_feels_label.setText(f"Ощущается как: {data.feels_like}")
            self.additional_info_label.setText(
                f"Облачно.\n\nВетер: {data.wind_speed} м/c\n\nВлажность: {data.humidity}%"
            )

            self.menu_button.show()
            self.weather_image.show()
            self.temp_tabel.show()
            self.temp_feels_label.show()
            self.additional_info_label.show()
        except KeyError:
            self.city_label.setText(f'Похоже, города с названием "{self.edit_text.text()}" нет в наших данных.')
            self.error_message_label.show()

    def start_progress(self):
        self.progress_bar.show()
        for i in range(101):
            time.sleep(0.005)
            self.progress_bar.setValue(i)
        self.progress_bar.hide()

    def check_clouds(self, check):
        if check >= 60:
            pixmap = QPixmap('../images/cloudy4.jpg')
            self.weather_image.setPixmap(pixmap)
        elif check <= 20:
            pixmap = QPixmap('../images/clear2.jpg')
            self.weather_image.setPixmap(pixmap)
        else:
            pixmap = QPixmap('../images/pasmurno.jpg')
            self.weather_image.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()

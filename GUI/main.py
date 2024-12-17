import sys
import datetime
import time

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QGridLayout
from PyQt6 import QtCore, QtGui, QtWidgets
import locale

locale.setlocale(
    category=locale.LC_ALL,
    locale="Russian"  # Note: do not use "de_DE" as it doesn't work
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather For Snakes")
        self.setEnabled(True)
        self.setWindowTitle("WeatherForSnakes")
        self.setFixedSize(1280, 720)
        self.setWindowIcon(QtGui.QIcon('snake.jpeg'))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(17, 52, 74))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        self.setPalette(palette)

        self.lbl1 = QLabel("Добро пожаловать на сервис", self)
        self.lbl1.setGeometry(0, 250, 1280, 200)
        self.lbl1.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.lbl1.setStyleSheet(
            # Шрифт
            'color: #fae1c2;'
            'font-family: Noto Serif;'
            'font-size: 26px;'
        )

        self.lbl2 = QLabel("Weather For Snakes", self)
        self.lbl2.setGeometry(0, 300, 1280, 400)
        self.lbl2.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.lbl2.setStyleSheet(
            # Шрифт
            'color: #fae1c2;'
            'font-family: Noto Serif;'
            'font-size: 32px;'
        )

        self.pushButton = QPushButton("Продолжить", self)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.pushButton.setGeometry(QtCore.QRect(350, 510, 600, 50))
        self.pushButton.setStyleSheet(
            # Границы, цвет
            'background-color: #f9df76;'

            # Шрифт
            'color: #000000;'
            'font-family: Noto Serif;'
            'font-size: 24px;'
        )
        self.pushButton.clicked.connect(self.show_mywindow)

    def show_mywindow(self):
        self.ui = MyWindow()
        self.ui.show()
        self.hide()

    def show_mywindow2(self):
        self.ui = MyWindow()
        self.ui.show()


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather For Snakes")
        self.setFixedSize(1280, 720)
        self.setWindowIcon(QtGui.QIcon('snake.jpeg'))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(17, 52, 74))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        self.setPalette(palette)

        self.logo = QtWidgets.QLabel(self)
        self.logo.setGeometry(250, 0, 700, 700)
        pixmap = QPixmap('snake.jpeg')
        self.logo.setPixmap(pixmap)

        self.edt = QLineEdit("", self)
        self.edt.setGeometry(50, 170, 600, 50)
        self.edt.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.edt.setStyleSheet(
            # Границы, цвет
            'background-color: #000000;'

            # Шрифт
            'color: #fae1c2;'
            'font-family: Noto Serif;'
            'font-size: 24px;'
            'font-weight: bold;'
        )

        self.pushButton = QtWidgets.QPushButton("Продолжить", self)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.pushButton.setGeometry(QtCore.QRect(650, 170, 200, 50))
        self.pushButton.setStyleSheet(
            # Границы, цвет
            'background-color: #f9df76;'

            # Шрифт
            'color: #000000;'
            'font-family: Noto Serif;'
            'font-size: 24px;'
        )
        self.pushButton.clicked.connect(self.button_clicked)

        self.lbl = QtWidgets.QLabel("Введите город:", self)
        self.lbl.setGeometry(50, 110, 400, 30)
        self.lbl.setStyleSheet(
            # Шрифт
            'color: #fae1c2;'
            'font-family: Noto Serif;'
            'font-size: 26px;'
        )

        self.pbar = QtWidgets.QProgressBar(self)
        self.pbar.hide()
        self.pbar.setGeometry(450, 450, 400, 30)
        self.pbar.setMaximum(100)
        self.pbar.setStyleSheet(
            # Шрифт
            'color: #ffffff;'
            'font-family: Noto Serif;'
            'font-size: 26px;'
        )

        self.time = QtWidgets.QLabel("", self)
        self.time.setGeometry(50, 40, 300, 50)
        self.time.setStyleSheet(
            # Шрифт
            'color: #fae1c2;'
            'font-family: Noto Serif;'
            'font-size: 26px;'
        )
        x = datetime.datetime.now()
        self.time.setText(x.strftime("%a, %d %b, %H:%M"))

        self.image = QtWidgets.QLabel(self)
        self.image.hide()
        self.image.setGeometry(0, 250, 1280, 600)

        self.rectangle = QtWidgets.QPushButton(self)
        self.rectangle.hide()
        self.rectangle.setGeometry(50, 300, 1180, 370)
        self.rectangle.setEnabled(False)
        self.rectangle.setStyleSheet(
            'background-color: rgba(28,28,28,100);'
        )

        self.temperature = QtWidgets.QLabel("", self)
        self.temperature.hide()
        self.temperature.setGeometry(600, 425, 200, 100)
        self.temperature.setStyleSheet(
            'color: #fae1c2;'
            'font-family: Noto Serif;'
            'font-size: 128px;'
        )

        self.temperature_feels = QtWidgets.QLabel("", self)
        self.temperature_feels.hide()
        self.temperature_feels.setGeometry(500, 300, 400, 100)
        self.temperature_feels.setStyleSheet(
            'color: #fae1c2;'
            'font-family: Noto Serif;'
            'font-size: 32px;'
        )

        self.additional_info = QtWidgets.QLabel("", self)
        self.additional_info.hide()
        self.additional_info.setGeometry(330, 550, 700, 100)
        self.additional_info.setStyleSheet(
            'color: #fae1c2;'
            'font-family: Noto Serif;'
            'font-size: 32px;'
        )

        layout = QGridLayout(self)
        layout.addWidget(self.temperature)

    def button_clicked(self):
        self.rectangle.hide()
        self.image.hide()
        self.temperature.hide()
        self.temperature_feels.hide()
        self.additional_info.hide()
        if self.edt.text() == 'Москва':
            self.startProgress()

            # Все значения здесь должны подставляться из API, пока просто тестовые данные стоят
            self.checkClouds("cloudy")
            self.temperature.setText("-7")
            self.temperature_feels.setText("Ощущается как: " + "-9")
            self.additional_info.setText("Облачно." + "  " + "Ветер: " + "7" + " м/c" + "  " + "Влажность: " + "15%")

            self.rectangle.show()
            self.image.show()
            self.temperature.show()
            self.temperature_feels.show()
            self.additional_info.show()

    def startProgress(self):
        self.pbar.show()
        for i in range(101):
            time.sleep(0.005)
            self.pbar.setValue(i)
        self.pbar.hide()

    def checkClouds(self, check):
        if check == "cloudy":
            pixmap = QPixmap('cloudy4.jpg')
            self.image.setPixmap(pixmap)
        elif check == "clear":
            pixmap = QPixmap('clear2.jpg')
            self.image.setPixmap(pixmap)
        else:
            pixmap = QPixmap('pasmurno.jpg')
            self.image.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()

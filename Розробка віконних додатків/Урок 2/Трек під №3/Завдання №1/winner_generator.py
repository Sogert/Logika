#підключення бібліотек
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
import sys
#створення елементів інтерфейсу
app = QApplication(sys.argv)

main_window = QWidget()
main_window.show()

text = QLabel("Натисни, щоб дізнатись переможця")
number = QLabel("?")
button = QPushButton("Згенерувати")

#прив'язка елементів до вертикальної лінії
vLayout = QVBoxLayout
vLayout.addWidget(text, alignment=Qt.AlignCenter)
vLayout.addWidget(number)
vLayout.addWidget(button)
#обробка подій

#запуск додатку
app.exec_()
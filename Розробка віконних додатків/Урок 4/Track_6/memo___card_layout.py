''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
from memo___app import app 

# віджети, які треба буде розмістити:
# кнопка повернення в основне вікно 
btn_menu = QPushButton("Menu")
# кнопка прибирає вікно і повертає його після закінчення таймера
btn_relax = QPushButton("Relax")
# введення кількості хвилин
box_minutes = QSpinBox()
box_minutes.setValue(30)
# кнопка відповіді "Ок" / "Наступний"
btn_answer = QPushButton("Answer")
# текст питання
question_label = QLabel("What word is correct?")
# Опиши групу перемикачів
rptn_1 = QRadioButton("")
rptn_2 = QRadioButton("")
rptn_3 = QRadioButton("")
rptn_4 = QRadioButton("")
radioGroupBox = QGroupBox("answer options")
radioGroup = QButtonGroup()
radioGroup.addButton(rptn_1)
radioGroup.addButton(rptn_2)
radioGroup.addButton(rptn_3)
radioGroup.addButton(rptn_4)
# Опиши панень з результатами

# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card

# Результат роботи цього модуля: віджети поміщені всередину layout_card, який можна призначити вікну.
def show_result():
    ''' показати панель відповідей '''
    pass

def show_question():
    ''' показати панель запитань '''
    pass

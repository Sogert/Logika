from memo___card_layout import *
from PyQt5.QtWidgets import QWidget
from random import shuffle # дозволяє здійснити перемішування відповідей в картці запитання

card_width, card_height = 600, 500 # початкові розміри вікна "картка"

def show_data():
    ''' показує на екрані потрібну інформацію '''
    pass

def check_result():
    ''' перевірка чи правильна відповідь обрана
   якщо відповідь було обрана, то надпис "вірно/невірно" отримує потрібне 
   значення і показується на панелі відповідей '''
    pass

win_card = QWidget()
#тут повинні бути параметри вікна
win_card.resize(card_width, card_height)
win_card.setWindowTitle("Memory Card")
win_card.move(0, 0)
win_card.show()
app.exec_()
class Widget():
    #властивості класа (в конструкторі)
    def __init__(self, text, x_place, y_place):
        self.text = text
        self.x = x_place
        self.y = y_place
    #методи
    def print_text(self):
        print("Напис:", self.text)
        print("Розташування: ", self.x, self.y)

class Button(Widget):
    #доповнені властивості класа (в конструкторі)
    def __init__(self, text, x_place, y_place, status_button):
        super().__init__(text, x_place, y_place)
        self.is_clicked = status_button
    def click(self):
        self.is_clicked = True
        print("Ви зареєстровані") 

    #нові методи

#створи екземпляр класа Button
button1 = Button('chdy', 50, 50, False)
button1.print_text()
#якщо на питання «Хочете зареєструватися?» користувач відповів «так», то застосуйте метод click
answer = input("Would you to register? \n")
if answer == 'yes':
    button1.click()
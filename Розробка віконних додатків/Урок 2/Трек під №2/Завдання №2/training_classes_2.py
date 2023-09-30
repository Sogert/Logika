class Title:
    def __init__(self, title_text, x, y):
        #конструктор
        self.text = title_text
        self.x_place = x
        self.y_place = y
        self.secretiveness = False
        #методи
    def info_text(self):
        print("Кнопка: ")
        
    def hide(self):
        self.secretiveness = True
    def show(self):
        self.secretiveness = False

    #створи два написи
    #приховай другий напис
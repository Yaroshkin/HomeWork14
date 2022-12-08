#Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить 
# в полях класса: название модели, год выпуска, произво-
# дителя, объем двигателя, цвет машины, цену. Реализуйте 
# методы класса для ввода данных, вывода данных, реа-
# лизуйте доступ к отдельным полям через методы класса. 

class Human:
    def __init__(self, name_model, year, made_in, engine_volume, color_car, price):
        self.name_model = name_model
        self.year = year
        self.made_in = made_in
        self.engine_volume = engine_volume
        self.color_car = color_car
        self,price = price
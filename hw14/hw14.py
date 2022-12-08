#Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить 
# в полях класса: название модели, год выпуска, произво-
# дителя, объем двигателя, цвет машины, цену. Реализуйте 
# методы класса для ввода данных, вывода данных, реа-
# лизуйте доступ к отдельным полям через методы класса. 

class Car:
    def __init__(self, name_model, year, made_in, engine_volume, color_car, price):
        self.name_model = name_model
        self.year = year
        self.made_in = made_in
        self.engine_volume = engine_volume
        self.color_car = color_car
        self.price = price

enter_name = input("Enter name: ")
enter_year = input("Year: ")
enter_made = input("Made in: ")
enter_engine = input("Engine motor: ")
enter_color = input("Color car: ")
enter_price = input("Price: ")

car1 = Car(enter_name,enter_year,enter_made,enter_engine,enter_color,enter_price)
with open("output.txt",'w') as f:
    f.write(f"Model {car1.name_model}, Year of admission {car1.year}, Car price {car1.price}")


# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в 
# полях класса: название книги, год выпуска, издателя, 
# жанр, автора, цену. Реализуйте методы класса для ввода 
# данных, вывода данных, реализуйте доступ к отдельным 
# полям через методы класса.

class Book:
    def __init__(self, name_book, year, edition, genre, author, price):
        self.name_book = name_book
        self.year = year
        self.edition = edition
        self.genre = genre
        self.author = author
        self.price = price
        


# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в 
# полях класса: название стадиона, дату открытия, страну, 
# город, вместимость. Реализуйте методы класса для ввода 
# данных, вывода данных, реализуйте доступ к отдельным 
# полям через методы класса.Домашнее задание

'''Tworzenie klasy pies'''

# class Dog():
#         """Prosta próba modelowania psa."""
#         def __init__(self, name, age):
#                 """Inicjalizacja atrybutów name i age."""
#                 self.name = name
#                 self.age = age
#
#         def sit(self):
#                 """Symulacja, że pies siada po otrzymaniu polecenia."""
#                 print(self.name.title() + " teraz siedzi.")
#
#         def roll_over(self):
#                 """Symulacja, że pies kładzie się na plecy po otrzymaniu polecenia"""
#                 print(self.name.title() + " teraz położył sie na plecy")
#
# my_dog = Dog("allie","6")
# your_dog = Dog("Memi","9")
#
# print("Mój pies ma na imię " + my_dog.name.title())
# my_dog.sit()
# my_dog.roll_over()
# your_dog.sit()

'''Zrób to sam 9.1, 9.2'''
#
# class Restaurant():
#         def __init__(self, restaurant_name, cuisine_type):
#                 self.restaurant_name = restaurant_name
#                 self.cuisine_type = cuisine_type
#
#         def describe_restaurant(self):
#                 print(self.restaurant_name +" "+ self.cuisine_type)
#
#         def open_restaurant(self):
#                 print(f"Restauracja {self.restaurant_name} jest czynna od pon-pt w godzinach 12-22")
#
# Pino_Garden = Restaurant("Pino Garden", "Kuchnia włoska")
# Pino_River = Restaurant("Pino River", "Kuchnia śródziemnomorska")
# Pino_Italia = Restaurant("Pino Italia", "Kuchania neapolitańska")
#
# # Restaurant_list = [Pino_Garden, Pino_River,Pino_Italia]
# Pino_Garden.describe_restaurant()
# Pino_Garden.open_restaurant()
# Pino_River.describe_restaurant()
# Pino_River.open_restaurant()
# Pino_Italia.describe_restaurant()
# Pino_Italia.open_restaurant()

'''Zrób to sam 9.3'''
#
# class User():
#         def __init__(self, first_name, last_name, date_of_birth, country):
#                 self.first_name = first_name
#                 self.last_name = last_name
#                 self.date_of_birth = date_of_birth
#                 self.country = country
#
#         def describe_user(self):
#                 print(f"A teraz kilka słów o użytkowniku, jego imię to {self.first_name}, nazwisko to {self.last_name}, pochodzi z {self.country}, jego data urodzenia to {self.date_of_birth}")
#
#         def greet_user(self):
#                 print(f"Witaj {self.first_name}, wiem, że pochodzisz z {self.country} to bardzo pięne miejsce")
#
#
# Anna = User("Anna","Jamróz","04-10-1995","Polska")
# Anna.describe_user()
# Anna.greet_user()

'''Praca z klasami i egzemplarzami'''

class Car():
        """Prosta próba zaprezentownia samochodu"""

        def __init__(self, make, model, year, odometer_reading):
                 """Inicjalizacja atrybutów opisujących samochód"""
                self.make = make
                self.model = model
                self.year = year
                self.odometer_reading = odometer_reading

        def get_descriptive_name(self):
                """Zwrot elegancko sformułowanego opisu samochodu"""
                long_name = str(self.year)+" "+ self.make +" "+ self.model
                return long_name.title()

        def read_odometer(self):
                """Wyświetla informację o przebiegu samochodu"""
                print(f"Ten samochód ma przebieg {self.odometer_reading} km")


my_new_car = Car("audi", "a4", "2016",2563256)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer



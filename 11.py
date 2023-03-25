'''Utwórz klasę Vehicle bez żadnych zmiennych i metod.'''
# class Vehicle:
#         pass
'''Klasa o nazwie MyClass z atrybutem o nazwie x'''
# class MyClass:
#         x = 5
# p1 = MyClass
# print(p1.x)

'''Klasa (class) dotycząca wyimaginowanego inwentarza odrzutowców jest już dla Was zdefiniowana. Również instancja tej klasy Jets jest stworzona i przypisana do zmiennej first_item. Wydrukuj name z first_item.'''
# class Jets:
#
#         def __init__(self, name, origin):
#                 self.name = name
#                 self.origin = origin
#
# first_item = Jets("Boeing 747", "US")
#
# print(first_item.name)

'''Tym razem wydrukuj origin z first_item.'''

# class Jets:
#
#         def __init__(self, name, origin):
#                 self.name = name
#                 self.origin = origin
# first_item = Jets("Boeing 747", "US")
#
# b=first_item.origin
# print(b)

'''Utwórz klasę Vehicle z atrybutami instancji max_speed i mileage.'''
# class Vehicle:
#         def __init__(self, max_speed, mileage):
#                 self.max_speed = max_speed
#                 self.mileage = mileage
# modelX = Vehicle(240, 18000)
#
# print(modelX.max_speed, modelX.mileage)

'''Utwórz klasę Car z dwoma atrybutami instancji:

.color, który przechowuje nazwę koloru samochodu jako ciąg testowy (str)
.mileage, który przechowuje liczbę kilometrów przejechanych przez samochód jako liczbę całkowitą (int)'''
# class Car:
#         def __init__(self, color, mileage):
#                 self.color = color
#                 self.mileage = mileage
# Car1 = Car("niebieski",200)
# Car2 = Car('czerwony',400)
#
# for car in (Car1, Car2):
#         print(f"{car.color} samochód ma {car.mileage:,} kilometrów przebiegu.")

# class Parrot:
#         pass
#
# obj = Parrot()
# print(type(obj))

# class Parrot:
#
#         # atrybuty instancji
#         def __init__(self, name, age):
#                 self.name = name
#                 self.age = age
#
#         # metoda instancji
#         def sing(self, song):
#                 return self.name + " śpiewa " + song
#
#         def dance(self):
#                 return self.name + " teraz tańczy"

# utworzenie wystąpienia obiektu
# blu = Parrot("Blu", 10)
# # wywołanie naszych metod instancji
# print(blu.sing("'Happy'"))
# print(blu.dance())

'''Konto Bankowe'''

# class KontoBankowe:
#     def __init__(self, nazwa, stan = 0):
#         self.nazwa = nazwa
#         self.stan = stan
#
#     def info(self):
#         print("nazwa:", self.nazwa)
#         print("stan:", self.stan)
#
#     def wyplac(self, ilosc):
#         self.stan -= ilosc
#
#     def wplac(self, ilosc):
#         self.stan += ilosc

'''Klasa (class) dotycząca wyimaginowanego inwentarza odrzutowców jest już dla Was zdefiniowana. Również instancja tej klasy Jets jest stworzona i przypisana do zmiennej first_item. Wydrukuj name z first_item.'''
#
# class Jets:
#
#
#     def __init__(self, name, origin):
#         self.name = name
#         self.origin = origin



# first_item = Jets("Boeing 747", "US")
#
#
# a = first_item.name
# b = first_item.origin
# print(a,b)

'''Najpierw utwórz klasę Car z atrybutami instancji .color i .mileage:'''

# class Car:
#         def __init__(self,color ,mileage):
#                 self.color = color
#                 self.mileage = mileage
#
# car1 = Car("niebieski",2000)
# car2 = Car("Red",30000)
# car3 = Car("niebieski",2000)
# car4 = Car("Red",30000)
#
# for car in [car1, car2, car3,car4]:
#         print(car.color, "samochód ma", car.mileage,"przebiegu")

# class Reversion:
#         def reverse(self, tekst):
#                 return teskt[::-1]
# obiekt = Reversion()
# obiekt.reverse("hello .py")

# class Tekst:
#         def get_word(self):
#                 self.word = input("Podaj ciąg tekstowy:")
#
#         def print_string(self):
#                 print(self.word.upper())
#
# obiekt = Tekst()
#
# obiekt.get_word()
# obiekt.print_string()

'''Przykład klasy - konto bankowe'''
#
# class KontoBankowe():
#
#
#     """Atrubuty instancji"""
#     def __init__(self, nazwa, stan = 0):
#         self.nazwa = nazwa
#         self.stan = stan
#
#     """Metoda instancji"""
#     def info(self):
#         print("nazwa:", self.nazwa)
#         print("stan:", self.stan)
#
#     def wyplac(self, ilosc):
#         self.stan -= ilosc
#
#     def wplac(self, ilosc):
#         self.stan += ilosc
#
# jk = KontoBankowe("Jan Kowalski",1000)
# jk.info()
# jk.wplac(100)
# jk.wyplac(200)
# jk.info()





'''Napisz klasę Pythona o nazwie Rectangle skonstruowaną na podstawie długości i szerokości oraz metody, która obliczy pole powierzchni prostokąta.'''
# a,b=0,1
# while b<10:
#         print(b),
#         a,b=b,a+b


'''Instancje odrzutowców'''

class Jest():
    def __init__(self, name, origin, quantity):
        self.name = name
        self.origin = origin
        self.quantity = quantity


first_item = Jest("Boeing 747", "US",87)
second_item = Jest("Airbus A380", "EU",98)
third_item = Jest("Embraer 195", "BR",96)

fleet = [first_item.name,second_item,third_item]

print(fleet)

total = first_item.quantity+second_item.quantity+third_item.quantity
print("Suma samolotów:", total)
jests = [Jest("Boeing 747", "US",87), Jest("Airbus A380", "EU",98), Jest("Embraer 195", "BR",96)]
total=0
for item in jests:
    total += item.quantity
print("Suma samolotów:", total)

numbers = [1, 2]
total = 0
for item in numbers:
    total += item.real
print("Suma części rzeczywistych:", total)

'''Pokojowa nagroda Nobla trafia do Bangladeszu'''




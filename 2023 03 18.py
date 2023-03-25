'''Utwórz klasę Temperature. Wykonaj dwie metody:
convert_fahrenheit - weźmie ona stopnie Celsjusza i wydrukuje je w Fahrenheitach.
convert_celsius - weźmie ona stopnie Fahrenheita i zamieni je na stopnie Celsjusza.'''

# class Temperature():
#     def farenhait(self, celcius):
#         return celcius*(9/5)+32
#
#     def celcius(self, farenhait):
#         return (farenhait-32)*(5/9)
#
# temp = Temperature()
#
# print(temp.farenhait(8))
# print(temp.celcius(8))

'''Utwórz klasę Student i zainicjuj ją imieniem/nazwiskiem (name) i numerem indeksu (roll). Klasa powinna też mieć atrybuty: wiek (age) i oceny (marks). Utwórz metody:
display - powinna wyświetlać wszystkie informacje o studencie.
set_age - powinna przypisywać wiek (age) studentowi.
set_marks - powinna wystawiać oceny (marks) studentowi (niech to będzie dla uproszczenia jedna ocena).'''

# class Student():
#     def __init__(self,name, roll):
#         self.name = name
#         self.roll = roll
#         self.age = None
#         self.marks = None
#
#     def display(self):
#         print(f"Student name is {self.name}, roll: {self.roll} age: {self.age} marks{self.marks}")
#
#     def set_age(self,age):
#         self.age = age
#
#     def set_marks(self, marks):
#         self.marks = marks
#
# obj = Student("Karl", "34567")
#
# (obj.display())
#
# obj.set_age(25)
# obj.set_marks(4)
# (obj.display())
#


'''Utwórz klasę Time i zainicjuj ją godzinami i minutami.
Utwórz metodę add_time, która powinna wziąć dwa obiekt Time i dodać je. Np. - (2 godz. i 50 min) + (1 godz. i 20 min) to (4 godz. i 10 min)
Stwórz metodę display_time, która powinna wypisać czas.
Utwórz metodę display_minute, która powinna wyświetlać łączną liczbę minut w Time. Np. - (1 godz. 2 min) powinno wyświetlać 62 minuty.'''
#
# class Time():
#     def __init__(self, hour,min):
#         self.hour = hour
#         self.min = min
#
#     def display_time(self):
#         print(f"Jest godzina {self.hour} i {self.min} min")
#
#     def display_min(self):
#         print(f"Mamy {(self.hour*60)+self.min} minut")
#
#     def add_time(self, h1, h2):
#         h3 = Time(0,0)
#         h3.min = (h1.min +h2.min) % 60
#         h3.hour = h1.hour + h2.hour + ((h1.min +h2.min)//60)
#         return h3
#
# objTime = Time(2,10)
# objTime2 = Time(3,8)
# objTime.display_time()
# objTime.display_min()
# newTime= objTime.add_time(objTime,objTime2)
# newTime.display_time()

'''Napisz definicję klasy Point. Obiekty z tej klasy powinny mieć:
metodę show, aby wyświetlić współrzędne punktu,
metodę move, aby zmienić te współrzędne,
metodę dist, która oblicza odległość między 2 punktami.
Zwróć uwagę, jak można obliczyć odległość między 2 punktami p(p1, p2) i q(q1, q2):'''

# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def show(self):
#         print(self.x, self.y)
#
#     def move(self,x,y):
#         self.x += x
#         self.y += y
#
#     def dist(self,p1,p2):
#         px = p1.x - p2.x
#         py = p1.y - p2.y
#         return ((px**2+py**2)**1/2)
#
# obj = Point(2,5)
# obj2 = Point(3,9)
# obj.show()
# obj.move(5,6)
# obj.show()
# print(obj.dist(obj,obj2))

'''Dziedziczenia'''
#
# class KontoBankowe:
#     def __init__(self, nazwa, stan=0):
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
#
#
# class KontoDebetowe(KontoBankowe):
#     def __init__(self, nazwa, stan=0, limit=0):
#         KontoBankowe.__init__(self, nazwa, stan)
#         self.limit = limit
#
#     def wyplac(self, ilosc):
#         """Jeżeli stan konta po operacji przekroczyłby limit, przerwij."""
#         if (self.stan - ilosc) < (-self.limit):
#             print("Brak srodkow na koncie")
#         else:
#             KontoBankowe.wyplac(self, ilosc)
#
# account = KontoDebetowe("Jan Nowak", 0, 1000)
# account.info()
# account.wplac(500)
# account.info()
# account.wyplac(1000)
# account.info()
# account.wyplac(1000)
# account.info()

'''Figura - dziedziczenie'''
import math


class Figura:
    def obwod(self):  # L
        """Obliczanie obwodu."""
        raise NotImplementedError

    def pole(self):  # S/P
        """Obliczanie pola powierzchni."""
        raise NotImplementedError


# class Kolo(Figura):
#     def __init__(self, r):
#         self.r = r
#
#     def obwod(self):
#         return 2 * math.pi * self.r
#
#     def pole(self):
#         return math.pi * self.r ** 2
#
# f1 = Kolo(5)
# print(f1.obwod())
# print(f1.pole())

class Trojkat(Figura):
    def __init__(self,a):
        self.a = a
        self.h = math.sqrt((a**2)/2)

    def pole(self):
        return



class Prostokat(Figura):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def obwod(self):
        return 2 * (self.a + self.b)

    def pole(self):
        return self.a * self.b
f3 = Prostokat(2, 5)
print(f3.obwod())
print(f3.pole())

class Kwadrat(Prostokat):
    def __init__(self, a):
        self.a = a
        # trik, dzięki któremu możemy dziedziczyć wprost
        # z prostokąta i nie musimy wypełniać metod `obwod` i `pole`
        self.b = a
f4 = Kwadrat(5)
print(f4.obwod())
print(f4.pole())

class Rownoleglobok(Figura):
    def __init__(self,a,b,h):
        self.a, self.b, self.h =a, b, h

    def obwod(self):
        return 2*self.a +2*self.b

    def pole(self):
        return self.a * self.h
f5 = Rownoleglobok(2 ,4,3)
print(f"Obwod to: {f5.obwod()} Pole to: {f5.pole()}")

class TrapezProstokatny(Figura):
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h
        self.c = (h**2+(a-b)**2)**0.5

    def obwod(self):
        return self.a + self.b+self.c+self.h

    def pole(self):
        return round((self.a+self.b)*self.h/2)

f6 = TrapezProstokatny(2 ,4,3)
print(f"Obwod to: {f6.obwod()} Pole to: {f6.pole()}")

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

bus = Bus("buss",120,18000)
print(bus.name, bus.max_speed, bus.mileage)


class Vehicle:

    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass

bus = Bus("buss",120,18000)

print(bus.color)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2*(self.width + self.length)

    def area(self):
        return self.width+self.length

    def display(self):
        print("Długość prostokąta to: ", self.length)
        print("Szerokość prostokąta to: ", self.width)
        print("Obwód prostokąta to: ", self.perimeter())
        print("Pole prostokąta to: ", self.area())

class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(self, length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

myRectangle = Rectangle(7, 5)
myRectangle.display()
myParallelepipede = Parallelepipede(7, 5, 2)
print("Objętość Równoległościanu wynosi: ", myParallelepipede.volume())
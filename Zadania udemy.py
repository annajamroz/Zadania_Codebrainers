'''61 Zad'''

# hitsTitles =[ 'BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
# hitsTitles.append('CHILD IN TIME')
# hitsTitles.append('AGAIN')
# print(hitsTitles)

'''69 if'''

# age = 23
# if age >= 20:
#     print("You are adult and you can buy alcohol")
# else:
#     print("You are to young")
#
# isDrunk = True
#
# if age >=18 and not isDrunk:
#     print("You are adult and you can buy alcohol")
# else:
#     print("You are adult and you can buy alcohoffffffffffl")

# '''70'''
# itRains = True
# #
# if itRains:
#     print("stay home")
# else:
#     print("we go")

# print( "we stay at home" if itRains else "we go out")

# i = 1
# imax = 10
#
# while i <= imax  :
#     print("i like python")
#     i += 1
#
# else:
#     print("Nowa i: ",i)


# values = [10,43,12,48,12,11,18,98,57,28,19,27,49,19,74]
#
# i = 0
# max = len(values) -2
# while i<max:
#     # print(i, values[i],values[i+1], values[i+2])
#     if values[i] < values[i+1] and values[i+1] < values[i+2]:
#         print(values[i],values[i+1], values[i+2])
#     i +=1
'''84'''

# data = ['Error:File cannot be open',
#         'Error:No free space on disk',
#         'Error:File missing',
#         'Warning:Internet connection lost',
#         'Error:Access denied']

# for dat in data:
# class MyClass:
#         x = 5
#
# p1=MyClass()
# print(p1.x)
'''78'''
# cake_01_taste = 'vanilia'
# cake_01_glaze = 'chocolade'
# cake_01_text = 'Happy Brithday'
# cake_01_weight = 0.7
#
# cake_02_taste = 'tee'
# cake_02_glaze = 'lemon'
# cake_02_text = 'Happy Python Coding'
# cake_02_weight = 1.3
#
#
# def show_cake_info(taste, glaze, text, weight):
#         print('{} cake with {} glaze with text "{}" of {} kg'.format(
#                 taste, glaze, text, weight))
#
#
# show_cake_info(cake_01_taste, cake_01_glaze, cake_01_text, cake_01_weight)
# show_cake_info(cake_02_taste, cake_02_glaze, cake_02_text, cake_02_weight)

# cake_01 = {'taste':'vanilia','glaze':'chocolade','text':'Happy Brithday','weight':'0.7'}
# cake_02 = {'taste':'tee','glaze':'lemon','text':'Happy Python Coding','weight':'1.3'}
#
#
#
# def show_cake_info(cake):
#         print('{} cake with {} glaze with text "{}" of {} kg'.format(
#         cake['taste'], cake['glaze'], cake['text'], cake['weight']))
#
# show_cake_info(cake_01)
# show_cake_info(cake_02)

# class Car:
#         def __init__(self, brand, model, isAirBagOk, IsPaintingOk, isMechanicalOk):
#                 self.brand = brand
#                 self.model = model
#                 self.isAirBagOk = isAirBagOk
#                 self.IsPaintingOk = IsPaintingOk
#                 self.isMechanicalOk  = isMechanicalOk
#
# car_01 = Car("Seat","Ibiza",True,True,True)
# car_02 = Car("Opel","Astra",True,False,True)
#
# print(car_02.brand)

# class Cake:
#         def __init__(self,name, kind, taste,additives, filling):
#                 self.name = name
#                 self.kind = kind
#                 self.taste = taste
#                 self.additives = additives
#                 self.filling = filling
#
# cakeStrawbery
# cakeChocolate

'''Zadanie z kodołamacz'''
# class Osoba:
#         def __init__(self, name, surname, age):
#                 self.name = name
#                 self.surname = surname
#                 self.age = age
#
#         def przedstaw_sie(self):
#                 print(f"Jestem{self.name} {self.surname}. Mam {self.age} lat")
#
#         def urodziny(self):
#                 wiek_przed = self.age
#                 self.age += 1
#                 return wiek_przed
#
# Jan = Osoba("Jan", "Nowak", "40")
# Adam  =Osoba("Adam","Kowalski","68")
#
# # wywołuje metodę przedstaw się
#
# Jan.przedstaw_sie()
# Adam.przedstaw_sie()
#
# Jan.urodziny(31)
'''84 Zaawansowany puthon klasy'''

class Car:

        numberOfCars = 0
        listOfCars = []
        def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicalOk, isOnSale):
                self.brand = brand
                self.model = model
                self.isAirBagOk = isAirBagOk
                self.isPaintingOk = isPaintingOk
                self.isMechanicalOk = isMechanicalOk
                self.__isOnSale = isOnSale
                Car.numberOfCars += 1
                Car.listOfCars.append(self)

        def IsDamaged(self):
                return not (self.isAirBagOk and self.isPaintingOk and self.isMechanicalOk)

        def GetInfo(self):
                print("{} {}".format(self.brand, self.model.upper()))
                print("Air bag - ok - {}".format(self.isAirBagOk))
                print("Painting - ok - {}".format(self.isPaintingOk))
                print("Mechanic - ok - {}".format(self.isMechanicalOk))
print(Car.numberOfCars, Car.listOfCars)
car_01 = Car('Seat','Ibiza', True, True, True,False)
car_02 = Car('Opel','Astra', True, False, True, False)
print(Car.numberOfCars, Car.listOfCars)
print(car_01.brand)
print(car_01.model)
print(car_01.IsDamaged())
print(car_02.GetInfo())
print('Check if object belongs to class:', isinstance(car_01, Car))
print('Check if ocject belongs to class using type', type(car_01) is Car)
print('Check class of an object using__class__:',car_01.__class__)
print(dir(car_01))
print(dir(Car))


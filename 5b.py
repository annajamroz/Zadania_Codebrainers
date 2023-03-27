'''Napisz program, który:

Będzie prosił użytkownika o podanie dwóch liczb, i
Wypisze:
Wynik ich dzielenia,
Resztę z dzielenia, oraz
Wynik dzielenia całkowitego'''

# a = input("Podaj piewsza liczbę:")
# b = input("Podaj drugą liczbę:")
# a = int(a)
# b = int(b)
# print("Wynik dzielenia tycz liczb to:", str(a/b))
# print('Reszta z dzielenia tych liczb to:', str(a%b))
# print("Wynik dzilenia całkowitego tych liczb to:", str(a//b))

'''Wydrukuj True, jeśli oba stwierdzenia są prawdziwe'''
# x = 5
# print(x > 3 and x < 10)

'''Wydrukuj wartość True, jeśli jedno ze stwierdzeń jest prawdziwe'''
# x = 7
# print(x > 4 or x < 3)

'''Ćwiczenie instrukcji if
Przypisz 8 do zmiennej x i 15 do zmiennej y
Utwórz 2 instrukcje warunkowe
Niech pierwsza wypisze: „Co najmniej jeden z warunków jest spełniony”, jeśli x jest większe niż 3 lub y jest parzyste
Niech drugi wypisze „Żaden warunek nie jest spełniony”, jeśli x jest mniejsze lub równe 3, a y jest nieparzyste
Zmień wartości przypisane do x i y i ponownie uruchom komórkę, aby sprawdzić, czy kod nadal działa'''

# x = 8
# y = 15
# if x>3 or y%2 == 0:
#     print("Conajmniej jeden z warunku jest spełniony")
#
# if x<3 and y%2 != 0:
#     print("Obydwa warunki nie sa spełnione")
#
'''Utwórz listę zawierającą imiona: prowadzącego oraz wszystkich osób uczestniczacych w kursie
Następnie ją posortuj alfabetycznie, oraz
Policz ile z osób na liście jest kobietami
W tym celu możesz sprawdzić czy imię kończy się na „a”'''

# name_list = ['Ania','Karolina','Katarzyna','Patryk','Marek','Konrad']
# print(sorted(name_list))
# count = 0
# for name in name_list:
#     if name[-1] == 'a':
#         count += 1
#     else:
#         pass
#
# print("Oto ilośc kobiet na liście:", count)

'''Poniżej znajdują się dwie listy. Napisz program w Pythonie konwertujący je na słownik w taki sposób, że pozycja z listy 1 jest kluczem, a pozycja z listy 2 jest wartością'''

# keys = ['Dziesieć', 'Dwadzieścia', 'Trzydzieści']
# values = [10, 20, 30]
#
# dict = dict(zip(keys,values))
# print(dict)

'''obaczmy ćwiczenie, które pomoże lepiej zrozumieć instrukcję pass
Umieść instrukcję pass, aby blok if nie zgłaszał błędu'''

# name = input("Proszę wpisać swoje imię.")
# # Wpisz swoją odpowiedź tutaj.
#
# if len(name) > 0:
#     print(name)
#
# else:
#     pass

'''Znajdź liczby, które są podzielne przez 7 i są wielokrotnością 5 w zakresie'''

# list_57 = []
#
# for x in range(1500,2701):
#     if x % 7 == 0 and x % 5 == 0:
#         list_57.append(x)
#
# print(list_57)

'''Wydrukuj pierwsze 10 liczb naturalnych za pomocą pętli while'''

# i=0
# while i<10:
#     i +=1
#     print(i)

'''Napisz program, który wydrukuje następujący wzór liczbowy za pomocą pętli.'''

# i=0
# list_i=[]
# for x in range(1,6):
#     i += 1
#     list_i.append(i)
#     print(list_i)
# i = 0
# for i in range(1,6):
#     for j in range(1, i+1):
#
#         print(j,end=' ')
#     print()

'''Oblicz sumę wszystkich liczb od 1 do podanej liczby'''
# x = input('Podaj liczbe:')
# x=int(x)
# count = 0
# for i in range(1,x+1):
#     count += i
#
# print(count)
#
# print(sum(range(1,x+1)))

'''Napisz program wypisujący tabliczkę mnożenia podanej liczby'''
# x = int(input('Podaj liczbę'))
# count = 0
# for i in range(1,11):
#     count = i*x
#     print(count)
'''Wyświetl liczby z listy za pomocą pętli??????'''
# numbers = [12, 75, 150, 180, 145, 525, 50]
# list_c = []
#
# for item in numbers:
#     if item > 500:
#         break
#     elif item > 150:
#         continue
#     # sprawdź, czy liczba jest podzielna przez 5
#     elif item % 5 == 0:
#         print(item)
'''Policz całkowitą liczbę cyfr w liczbie'''

# x = input("Podaj liczbę a powiem Ci ile ma cyfr")
#
# conter = 0
# print(len(x))

'''Wydrukuj następujący wzór'''

# n = 5
# k = 5
#
# for i in range(0,n+1):
#     for j in range(k-i,0,-1):
#         print(j,end=' ')
#     print()
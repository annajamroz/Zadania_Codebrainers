'''Biorąc pod uwagę ciąg o nieparzystej długości większej niż 7, zwróć łańcuch złożony z trzech środkowych znaków danego ciągu:
'''
# str1 = "Datatypes"
# middle_index = int(len(str1)/2)
# wynik = str1[middle_index-1:middle_index+2]
# print(wynik)
#
# str2 = "FullStack"
# middleindex2 = int((len(str2))/2)
# wynik2 = str2[middleindex2-1:middleindex2+2]
# print(wynik2)
# print(type(middleindex2))

'''Biorąc pod uwagę 2 ciągi, s1 i s2, utwórz nowy ciąg, dodając s2 w środku s1'''
# s1 = "FullStack"
# s2 = "Python"
# middle_index = int(len(s1)/2)
# s3 = s1[:middle_index]+s2+s1[middle_index:]
# print("Oto połączenie nowego ciągu:",s3)

'''Biorąc pod uwagę 2 ciągi, s1 i s2 zwróć nowy ciąg złożony z pierwszego, środkowego i ostatniego znaku każdego ciągu wejściowego'''
# s1 = "America"
# s2 = "Japan"
#
# first = s1[0]+s2[0]
# middles1 = int(len(s1)/2)
# middles2 = int(len(s2)/2)
# second = s1[middles1]+s2[middles2]
# third = s1[-1]+s2[-1]
#
# print(first+second+third)

'''Odwróć podany ciąg'''
# str1 = "Python"
# print(str1[::-1])

'''odwróć krotkę'''
# tuple1 = (10, 20, 30, 40, 50)
# print(tuple1[::-1])

'''dostęp do wartości 20 z krotki'''
# tuple1 = ("Pomarańczowy", [10, 20, 30], (5, 15, 25))
# print(tuple1[1][1])

'''Utwórz listę zawierającą imiona wszystkich kursantów
Następnie ją posortuj alfabetycznie, oraz
Sprawdź ile elementów ona zawiera'''

# name_list = ['Ania','Karolina','Katarzyna','Patryk','Marek','Konrad','Filip']
# print('Oto uporządkowana alfabetycznie lista',sorted(name_list))
# print('Oto liczba pozycji na liście', len(name_list))

'''Ćwiczenie — zamień dwie listy na słownik'''
# keys = ['Dziesieć', 'Dwadzieścia', 'Trzydzieści']
# values = [10, 20, 30]
#
# dict = dict(zip(keys,values))
# print(dict)

'''Ćwiczenie — dodaj listę elementów do zbioru'''
sample_set = {"Żółty", "Pomarańczowy", "Czarny"}
sample_list = ["Niebieski", "Zielony", "Czerwony"]

sample_set.update(sample_list)
print(sample_set)
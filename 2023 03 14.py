# Konstrukcja:  lambda agr1, arg2: arg1**arg2

# Pitagoras: lambda a, b: ((a*a)+(b*b)**0.5

# temperatury = [
#     37.6, 35.8, 37.6, 33.4, 34.1, 37.1, 35.9, 34.1, 37.1, 40.5, 38.5, 37.6,
#     35.8, 34.5, 36.4, 38.3, 37.5, 37.7, 34.0, 35.3, 35.7, 38.9, 34.8, 34.1,
#     39.6, 35.4, 34.7, 37.6, 38.4, 36.4, 39.8, 39.1, 37.1, 35.6, 36.8, 37.6,
#     36.7, 40.0, 38.0, 34.1, 35.5, 38.5, 36.1, 32.6, 32.9, 34.5, 41.0, 38.3,
#     33.7, 38.7, 36.9, 36.2, 33.7, 38.3, 35.3, 38.3, 40.1, 39.3, 38.2, 37.6,
#     39.1, 37.1, 34.4, 38.7, 35.8, 38.2, 38.2, 33.1, 37.8, 36.5, 37.6, 37.4,
#     34.3, 37.7, 36.0, 37.5, 37.6, 36.5, 31.3, 37.7, 40.3, 39.5, 35.7, 38.1,
#     34.7, 36.5, 34.3, 38.0, 37.0, 38.5, 39.4, 37.6, 41.7, 40.0, 38.4, 38.9,
#     34.2, 40.2, 34.3, 35.3  ]
#
# wynik = list(filter(lambda x: x >= 40.0, temperatury))
# print(wynik)
# wynik_sort = sorted(wynik)
# print(wynik_sort)


# ludzie = {'Jan': 40, 'Maria': 20}
# print(list(filter(lambda x: ludzie[x] < 30, ludzie)))

# temperatury = [
#     37.6, 35.8, 37.6, 33.4, 34.1, 37.1, 35.9, 34.1, 37.1, 40.5, 38.5, 37.6,
#     35.8, 34.5, 36.4, 38.3, 37.5, 37.7, 34.0, 35.3, 35.7, 38.9, 34.8, 34.1,
#     39.6, 35.4, 34.7, 37.6, 38.4, 36.4, 39.8, 39.1, 37.1, 35.6, 36.8, 37.6,
#     36.7, 40.0, 38.0, 34.1, 35.5, 38.5, 36.1, 32.6, 32.9, 34.5, 41.0, 38.3,
#     33.7, 38.7, 36.9, 36.2, 33.7, 38.3, 35.3, 38.3, 40.1, 39.3, 38.2, 37.6,
#     39.1, 37.1, 34.4, 38.7, 35.8, 38.2, 38.2, 33.1, 37.8, 36.5, 37.6, 37.4,
#     34.3, 37.7, 36.0, 37.5, 37.6, 36.5, 31.3, 37.7, 40.3, 39.5, 35.7, 38.1,
#     34.7, 36.5, 34.3, 38.0, 37.0, 38.5, 39.4, 37.6, 41.7, 40.0, 38.4, 38.9,
#     34.2, 40.2, 34.3, 35.3
# ]
#
# from statistics import mean
# sr_temp = mean(temperatury)
# print(sr_temp)
#
# odch = list(map(lambda x: round(x - sr_temp,2), temperatury))
# print(odch)
# from functools import reduce
# nums = [1, 2, 3, 4, 5]
# print(reduce(lambda a, b: a + b, nums))
# print(reduce(lambda a, b: a * b, [1, 2, 3, 4]))
'''Utwórz funkcję lambda, która przyjmuje jeden parametr (a) i zwraca go'''

# x = lambda a : a
# print(x(2))

'''Napisz program w Pythonie, aby utworzyć funkcję lambda, która dodaje 15 do podanej liczby przekazanej jako argument i zwraca to jako wynik. Następnie wydrukuj wynik.'''
# r = lambda a: a + 15
# print(r(10))

# m = lambda x,y: x*y
# print(m(2,5))

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# new_list = list(filter(lambda x: x%2!=0, nums))
# print(new_list)

# '''Znaleźć przecięcie'''
# array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
# array_nums2 = [1, 2, 4, 8, 9]
#
# print(list(filter(lambda x: x in array_nums2, array_nums1)))

# array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
# even_nums = lenfilter(lambda x: x%2!=0, nums)
'''Napisz program w Pythonie, aby znaleźć wartości o długości sześć na podanej liście za pomocą funkcji lambda i filter'''
# weekdays = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
#
# weekdays_6 = list(filter(lambda day: len(day)==6, weekdays))
# print(weekdays_6)

'''Napisz program w Pythonie, aby znaleźć liczby podzielne przez dziewiętnaście lub trzynaście z listy liczb za pomocą lambda i filter'''
# nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# wynik = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, nums))
# print(wynik)

'''Napisz program w Pythonie, aby znaleźć palindromy na podanej liście ciągów za pomocą lambda i filter
Palindrom – wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej
Przykładem palindromu jest: „kobyła ma mały bok”'''

# texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
# r = list(filter(lambda x: x == x[::-1], texts))
# print(r)
# from functools import reduce
#
# sample_names = ['antoni', 'Jakub', 'zuzanna', 'Julia', 'Jan', 'szymon']
# name = list(filter(lambda name: name[0].isupper(), sample_names))
# print(name)
# name_string = len(reduce(lambda x,y: x+y, name))
# print(name_string)
#
# name_l = len(name_string)
# print(name_l)

'''Napisz program w Pythonie podnoszący do kwadratu i sześcianu każdą liczbę z podanej listy liczb całkowitych, używając lambda i map'''

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# square = list(map(lambda n: n ** 2, nums))
# print(square)
# cube = list(map(lambda n: n ** 3, nums))
# print(cube)

'''Napisz program w Pythonie, aby dodać dwie podane listy za pomocą map i lambda'''

# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
#
# result = list(map(lambda x, y: x + y, nums1, nums2))
# print(result)

'''Napisz program w Pythonie, który za pomocą funkcji lambda mnoży każdą liczbę z podanej listy przez określoną liczbę
Wydrukuj wynik'''

# nums = [2, 4, 6, 9, 11]
# n = 2
#
# print(list(map(lambda x: x+n, nums)))

'''Napisz program w Pythonie, który usuwa liczby dodatnie z podanej listy liczb
Zsumuj liczby ujemne i wydrukuj wartość bezwzględną za pomocą tworzenia listy – ang. list comprehension
Wydrukuj wynik'''

# nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
# dod = abs(sum([ x for x in nums if x < 0]))
# print(dod)

'''Napisz program w Pythonie, aby:
Znaleźć liczby z podanego ciągu
Zapisać je na liście
Wyświetlić liczby w posortowanej formie
Użyj funkcji tworzenia listy – ang. list comprehension, aby rozwiązać problem'''

# str1 = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
# str1_num = str1.split()
# print(str1_num)
#
# new_list = [int(el) for el in str1_num if el.isdigit()]
# print(sorted(new_list))


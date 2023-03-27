'''Funkcja dodawania'''

# def add(x,y):
#     print("Oto funkcja, która sumuje dwie liczby")
#     print("x=",x,"y=",y)
#     return x+y
#
# print(add(6,8))

'''Funkcja w Pythonie do obliczania długości łańcucha'''

# def string_lenght(str):
#     count = 0
#     for char in str:
#         count += 1
#     return count
#
# print(string_lenght("gfdninkinknk"))

'''Funkcja w Pythonie, która zsumuje wszystkie elementy na liście'''

# list = [2,3,89,48,932,48,787,841]
#
# def sum_list(list):
#     sum_number = 0
#     for x in list:
#         sum_number += x
#     return sum_number
#
# print(sum_list([2,3,89,48,932,48,787,841]))

'''Funkcja w Pythonie, który mnoży wszystkie elementy na liście'''

# def multiply_list(list):
#     tot = 1
#     for x in list:
#         tot = tot*x
#     return tot
#
# print(multiply_list([2,3]))

'''Funkcja w Pythonie, aby uzyskać największą liczbę z listy'''

# def max_list(list):
#     list_max = list[0]
#     for x in list[1:]:
#         if x > list_max:
#             list_max = x
#     return list_max
#
# print(max_list([2,3,89,48,932,48,787,841]))

'''Funkcja w Pythonie, który zlicza liczbę znaków (częstotliwość znaków) w ciągu znaków'''

# def char_frequency(str):
#     dict = {}
#     for x  in str:
#         keys = dict.keys()
#         if x in keys:
#             dict[x] +=1
#         else:
#             dict[x] = 1
#     return dict
#
# print(char_frequency("gooolgke"))

'''Funkcja w Pythonie do zliczania ciągów znaków, w których długość ciągu wynosi 2 lub więcej, a pierwszy i ostatni znak są takie same z podanej listy ciągów'''

# def match_words(words):
#     sum = 0
#     for word in words:
#         if int(len(word))>2 and word[0]==word[-1]:
#             sum +=1
#     return sum
#
# print(match_words(['abc', 'xyz', 'aba', '1221']))

'''Funkcja Pythona do pobrania listy, posortowanej w porządku rosnącym według ostatniego elementu w każdej krotce z podanej listy niepustych krotek'''
# def last(n):
#     return n[-1]
#
# def sort_list_tuples(tuples):
#     return sorted(tuples,key=last)
#
#
# print(sort_list_tuples([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

'''Funkcja Pythona do pobrania ciągu znaków złożonego z pierwszych 2 i ostatnich 2 znaków z podanego ciągu'''
# def string_two(str):
#     if len(str)<2:
#         return ' '
#     else:
#         print(str[:2]+str[-2:])
#
# print(string_two('python'))

'''Napisz program, policzy silnię dla liczby n tj'''
# def recur_factorial(n):
#     if n == 1:
#         return 1
#     return n * recur_factorial(n-1)
#
# print(recur_factorial(7))
#
# def factorial(x):
#     s = 1
#     for i in range(1,x+1):
#         s *= i
#     return s
#
# print(factorial(7))

'''Funkcja w Pythonie, aby uzyskać najmniejszą liczbę z listy'''
def smallest_num_in_list(list):
    min_a = list[0]
    for a in list[1:]:
        if a < min_a:
            min_a = a
    return min_a
print(smallest_num_in_list([1, 2, -8, 0]))




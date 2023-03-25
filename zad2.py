'''Zadanie 1
Napisz program który wczyta wyrazy wczytane przez użytkownika i wypisze te które kończą się na 'a'.
'''

# words=input("Podaj słowa po przecinku: ")
# words_list=words.split(sep=',')
# print(words_list)
#
# word_list=[]
#
# for word in words_list:
#     if word[-1]=="a":
#         word_list.append(word)
#
#     else:
#         pass
# print(word_list)

'''Zadanie 2
Napisz program który wczyta zdanie napisane przez użytkownika i przetłumaczy je na Pig Latin.
Pig Latin - gra językowa oparta na języku angielskim.
Polega na przesunięciu pierwszej litery na koniec wyrazu i dodaniu końcówki "ay".'''

# userWord = input("Podaj słowa a zagramy: ")
# userList=userWord.split(sep=" ")
# newList=[]
# print(userList)
# print("Podałeś to słowo %s" % (userWord))
#
# for item in userList:
#     newWord = item[1:] + item[0]+"ay"
#     newList.append(newWord)
# print(newList)

'''Zadanie 3
Z podanych przez użytknownika wyrazów wypisz takie, które są dłuższe niż 5.'''

# words = input("Podaj słowa rodzlielająć je spacją:")
# wordsList = words.split(sep=" ")
# fiveList = []
#
# for word in wordsList:
#     if len(word) >= 5:
#         fiveList.append(word)
#     else:
#         pass
# print(fiveList)

'''Zadanie 4
Napisz program który z wyrazów podanych przez użytkownika wypisze te które są napisane wielkimi literami.'''
#
# words = input("Podaj słowa rodzlielająć je spacją:")
# wordsList = words.split(sep=" ")
# upperList = []
#
# for word in wordsList:
#     if word == word.upper():
#         upperList.append(word)
#     else:
#         pass
# print(upperList)

'''Zadanie 5
Napisz program który z wyrazów podanych przez użytkownika wypisze palindromy.'''

# words = input("Podaj słowa rodzlielająć je spacją:")
# wordsList = words.split(sep=" ")
# paliList = []
#
# for word in wordsList:
#     if word == word[::-1]:
#         paliList.append(word)
#     else:
#         pass
# print(paliList)

'''Zadanie 6
Napisz program który przyjmie wyrazy od użytkownika i wypisze je, jednak jeżeli wyraz ma parzystą ilość liter
to wypisz go wielkimi literami.
Przykład:
input:
daj ać ja pobruszę a ty poczywaj
output:
daj AĆ JA POBRUSZĘ a TY POCZYWAJ'''

# words = input("Podaj słowa rodzlielająć je spacją:")
# wordsList = words.split(sep=" ")
# upperList = []
#
# for word in wordsList:
#     if len(word) % 2 == 0:
#         upperList.append(word.upper())
#     else:
#         upperList.append(word)
# print(upperList)

'''Zadanie 7
Napisz program który znajdzie minimum i maksimum w liście liczb podanej przez użytkownika.
Przykład
input:
2 1 5 3 4 7 8 8 1
output:
maksimum: 8
minimum: 1'''

# numbers = input("Podaj cyfry po przecinku: ")
# numbersList = numbers.split(sep=",")
#
# print("Max to: " + max(numbersList, key=int))
# print("Min to: " + min(numbersList, key=int) )

'''Zadanie 8
Napisz program który działa jak `str.rfind` -znajduje pierwsze wystąpienie wzorca w stringu ale od prawej strony'''

# userWord = input("Podaj słowo: ")
# userLetter = input("Podaj szukaną literkę: ")
#
# def find(userWord, userLetter):
#
#      userWord.rfind("userLetter")

'''Zadanie 9
Napisz program który narysuje wzorek (użyć pętli!)'''
count = 0
for i in range(1,11):
     if i <= 5:
          count += 1
          print(count*"*")
     if i>5:
          count -= 1
          print(count*"*")





'''Zadanie 10
Napisz program który wypisze liczby od 1 do 50. Dla wielokrotności 3 wypisz `fizz`, dla wielokrotności 5 wypisz
`buzz`. Dla liczb które są wielokrotnością zarówno 3 i 5 wypisz `fizzbuzz`.'''

# items = range(51)
# for i in items:
#      if i % 3 == 0 and i % 5 == 0:
#           print('fizzbuzz')
#      elif i % 3 == 0:
#           print('fizz')
#      elif i % 5 == 0:
#           print('buzz')
#      else:
#           print(i)
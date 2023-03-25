'''Zadanie 1
Stwórz dwie zmienne `a` i `b` i przypisz do nich różne wartości. Napisz program który zamienia wartości
zmiennych miejscami.'''

# a=input("Podaj wartoś a : ")
# b=input("Podaj wartośc b: ")

# zmiana wartości zmiennych
# a, b = b, a
#
# print(a, b)

# DRUGIE ROZWIAZANIE
# a = int(input('Podaj wartość a: ')) # wczytujemy pierwszą liczbę i rzutujemy ją na int (na liczbę całkowitą)
# b = int(input('Podaj wartość b: ')) # wczytujemy pierwszą liczbę i rzutujemy ją na int
#
# # wykonujemy zamianę wartości zmiennych
# a, b = b, a
#
# print(a, b)

'''Zadanie 2
Napisz program który przyjmie trzy liczby i wypisze średnią z nich.'''
# a=input("Podaj wartość pierwszej liczby:")
# b=input("Podaj wartość drugiej liczby:")
# c=input("Podaj wartość trzeciej liczby:")
#
# d="Oto średnia arytmetyczna zpodanych liczb"
# e=(int(a)+int(b)+int(c))/3
#
# print(d,str(e))

'''Zadanie 3
Kupiłeś Bitcoiny i zastanawiasz się ile zarobisz. Napisz program, który:
- przyjmie wartość bitcoina w momencie zakupu;
- przyjmie procent wzrostu (lub spadku) wyrażony jako liczba z przedziału (-1, 1);
- wypisze aktualna wartość twoich bitcoinów i ile zyskałeś (straciłeś).'''

# bt=int(input("Podaj ilość bitcoin: "))
# growth=float(input('Podaj wartośc wzrostu: '))
#
# advantage=bt*(growth)
# print("Oto Twój wzrost: %d" %(advantage))

'''Zadanie 4
Napisz program który przyjmuje rozmiary działki i zwraca jej pole'''

# a=float(input("Podaj szerokośc działki: "))
# b=float(input("Podaj długośc działki: "))
#
# area=a*b
#
# print("Pole działki wynosi: %d" %(area))

'''Zadanie 5
Świetnie Ci idzie zarabianie na bitcoinach. Chcesz teraz zainwestować w inne kryptowaluty. Napisz program, który
przyjmie:
- ilość twojej gotówki;
- cenę bitcoina, etherum i litecoina;
- i zwróci ile za swoją gotówkę możesz kupić bitcoinów, etherum i litecoinów.'''

# cash=float(input("How much many do you have?: "))
# bitcoin=float(input("Enter the mount of bitcoins: "))
# etherum=float(input("Enter the amout of etherum: "))
# litecoin=float(input("Tnter the amount of litecoin: "))
#
# cashBt=float(cash/bitcoin)
# cashEt=float(cash/etherum)
# cashLi=float(cash/litecoin)
#
# print("You cen buy "+ str(cashEt)+ " etherum and " + str(litecoin) +" licecoin for your money")
#
'''Zadanie 6
Chcesz kupić laptopa z Chin, ale możliwe, że Urząd Celny doliczy Ci cło. Napisz prograPodaj wartość laptopam, który:
- przyjmie cenę laptopa
- procent cła
- i wypisze ile będziesz miał faktycznie do zapłaty'''

# laptopValue=float(input("Enter the value of the laptop: "))
# duty=float(input("Enter the value of duty i percent: "))
#
# print("You have to pay: "+str(laptopValue*duty)+" dolars")

'''Zadanie 7
W firmie w której pracujesz, premia jest wyliczana na podstawie Twojego stażu pracy. Za każdy przepracowany
rok pracy otrzymujesz ekstra 250zł. Napisz program, który przyjmie:
- podstawę twojego wynagrodzenia;
- staż pracy;Podaj wysokośc swojej pensji w PLN
- wypisz jakie dostaniesz wynagrodzenie wraz z premią.'''

# salary=float(input("Enter your salary in PLN: "))
# bonus=float(input("Enter your bonus: "))
# years=float(input("Years worked: "))
#
# print("Your salary is %d after %d years of service"%((salary+bonus*years),years))

'''Zadanie 8
Napisz program który zwróci cyfrę jedności podanej liczby.'''

# number=(input("Enthet the number: "))
# print((number[-1]))




a = 4

# IF
if a == 3:
    print("Then shalt thou count to three, no more, no less.")
    print("Three shall be the number thou shalt count, and the number of the counting shall be three.")
    print("Four shalt thou not count, neither count thou two, excepting that thou then proceed to three. ")
else:
    print('Not three')

if a == 3:
    print("three")
else:
    if a == 4:
        print("four")
    else:
        print('Not three or four')

n = int(input('Podaj liczbę'))
print(n)

# ELSE
if n == 1:
    print('Jaden')
elif n == 2:
    print('dwa')
elif n == 3:
    print('trzy')
elif n == 4:
    print('cztery')
elif n == 5:
    print('pięc')
else:
    print('tej liczby nie znam')

# Warunki logiczne

if (n == 17) or not (n == 17):
    print("Tertium non datur")
    print("Innej opcji nie ma")
n = 5
if n == 17 or n != 17:
    print("Tertium non datur")
    print("Innej opcji nie ma")

# := "Walrus" operator
if (i := int(input("podaj liczbę naturalną"))) % 2 == 0:
    print(f'{i} jest parzyste')
else:
    print(f'{i} jest nieparzyste')

# zadanie 1
# wczytaj liczbę 2 cyfrową -
# wypisz Dobra liczba jeśli suma jej cyfr dzieli się przez 7
# oraz liczba jest parzysta, a Zła liczba w przeciwnym wypadku
a = int(input("podaj liczbe"))
    b = a % 10
    c = a // 10
    i = b + c
    if (i % 7 == 0 and a % 2 == 0):
        print("liczba jest dobra")
    else:
    print("liczba jest zla")

# zadanie 2
# Wypisać wszystkie liczby od 1 do 100 które spełniają warunek z poprzedniego zadania

for a in range(1,100):
# a = int(input("podaj liczbe"))
    b = a % 10
    c = a // 10
    i = b + c
    if (i % 7 == 0 and a % 2 == 0):
        print(f"{a} liczba jest dobra")
    # else:
    #     print("liczba jest zla")

# Zadanie 3
# wczytaj przy użyciu input() liczbę; wypisz sumę jej cyfr
number = input()
suma = 0
for c in str(number):
       print(c,suma)
       suma += int(c) #suma = suma + c
print(suma)

# Zadanie 4
# wczytać z przez input liczbę,
# stworzyć choinkę o odpowiedniej wysokosci
n = int(input("wysokosc choinki"))
for i in range(n):
    print(f'{" "*(n-i)}{"*"*(2*i+1)}')
for i in range(n):
    if i == 2:
        break
    print(f'{" " * (n - i)}{"*" * (2 * i + 1)}')

# Zadanie 5
# stwórz pętle pobierającą napisy z wejścia aż do napotkania pustego napisu; wypisz listę posortowaną alfabetycznie wczytanych napisów
# stwórz pętle pobierającą liczby z wejścia aż do napotkania pustego napisu; wypisz ostatnią parzystą

l = []
while True:
    input ("wpisz cos albo enter")
    if (lst == ""):
        break
    lista.append(lst)
lista.sort(key=str)
print(lista)
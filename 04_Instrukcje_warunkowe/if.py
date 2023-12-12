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

lista = []
while True:
    napis = input ("wpisz cos albo enter")
    if napis == "":
        break
    lista.append(napis)
lista.sort()
print(lista)

# Zadanie 6
# Dla listy napisów pobranej w pętli z wejścia wypisać słownik ilości wystąpień napisów
# np. dla ['Ala', 'ma' 'kota', 'kota'] wypisać {'Ala': 1, 'ma': 1, ;'kota': 2}

s = {}
while True:
    wpis = input ("wpisz wyraz")
    if wpis == "":
        break
    #     "" to chodzi, że pusty napis i kończy pętlę, bo nic nie zostało wpisane

    n = s.get(wpis,0)
    n += 1
    s[wpis] = n
    print (s)


# Zadanie 7
# Dla wczytanej liczby z wejścia z zakresu 1-999 wypisać jej postać słowną
# np. dla 73 wypisać siedemdziesiąt trzy


nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięc"}
nastki = {0: "", 11: "jedenaście", 12: "dwanaście", 13: "trzynaście", 14: "czternaście", 15: "piętnaście", 16: "szesnaście", 17: "siedemnaście", 18: "osiemnaście",
                  19: "dziewiętnaście"}
dziesiatki = {0: "", 10: "dzisięć", 20: "dwadzieścia", 30: "trzydzieści", 40: "czterdzieści", 50: "pięćdziesiąt", 60: "sześćdziesiąt", 70: "siedemdziesiąt", 80: "osiemdzieiąt",
                  90: "dziewięćdzisiąt"}
setki = {0: "", 100: "sto", 200: "dwiescie", 300: "trzydzieści", 400: "czterdzieści", 500: "pięćdziesiąt", 600: "sześćdziesiąt", 700: "siedemdziesiąt", 800: "osiemdzieiąt",
                  900: "dziewięćdzisiąt"}

s = {}
n = int(input("wpisz liczbę"))
if n in range(11, 20):
    napis = nastki[n]
else:
    napis = dziesiatki[n - n % 10] + " " + nazwy_jednosci[n % 10]
print(napis)




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
setki = {0: "", 100: "sto", 200: "dwiescie", 300: "trzysta", 400: "czterysta", 500: "pięćset", 600: "sześćset", 700: "siedemset", 800: "osiemset",
                  900: "dziewięćset"}

s = {}
n = int(input("wpisz liczbę"))
napis = setki[n-n%100]
n%= 100
if n in range(11, 20):
    napis += nastki[n]
else:
    napis += dziesiatki[n - n % 10] + " " + nazwy_jednosci[n % 10]
print(napis)

# drugi sposob
nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
nazwy_nast = {10: "dziesięć", 11: "jedenaście", 12: "dwanaście", 13: "trzynaście", 14: "czternaście", 15: "piętnaście", 16: "szesnaście", 17: "siedemnaście", 18: "osiemnaście",
                  19: "dziewiętnaście"}
nazwy_dziesiatek = {2: "dwadzieścia", 3: "trzydzieści", 4: "czterdzieści", 5: "pięćdziesiąt", 6: "sześćdziesiąt", 7: "siedemdziesiąt", 8: "osiemdziesiąt", 9: "dziewięćdziesiąt"}

nazwy_setek = {1: "sto", 2: "dwieście", 3: "trzysta", 4: "czterysta" , 5: "pięćset", 6: "sześćset", 7: "siedemset", 8: "osiemset", 9: "dziewięćset"}

liczba = int(input("Wpisz cyfre"))

g = int(liczba) // 100
d = (liczba % 100 ) // 10
j = liczba % 10
lista_2 = []
if g != 0:
    lista_2.append(nazwy_setek[g])
if d == 1:
    lista_2.append(nazwy_nast[liczba % 100])
else:
    lista_2.append(nazwy_dziesiatek[d])
    lista_2.append(nazwy_jednosci[j])
print (" ".join(lista_2) )

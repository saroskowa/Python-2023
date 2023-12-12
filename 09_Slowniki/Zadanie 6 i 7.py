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

# stworzyc słownik { 'first': funkcja1, 'second': funkcja2 },
# wczytać przez input klucz, wywołać funkcję


# to na brudno do pokombinowania
def f11():
    print("Jestem funkcja1")

def f22():
    print("jestem funkcja_2")

s = {1: "funkcja1", 2: "funkcja_2"}
inp=input("wpisz 1 lub 2"))
f=s[inp]
f()
# .............................

def f1(n="OK"):
    """
    ta funckja wpisuje 'OK'
    return: OK
    """
    print(n)

def f2(x="NOK"):
    print(x)

s= {'f1':f1, 'f2':f2}
inp=input("Klucz f1 czy f2")
f=s[inp]
f()

# zadanie 11
# stworzyc funckcję alphabet_range działająca jak range ale dla liter (z trzema parametrami - start, end, step)
# przykład: alphabet_range('E') -> ['A', 'B', 'C', 'D'] - albo jeszcze lepiej generator
# użyć
# ord - podaje kod calkowity danego znaku
# chr - podaje znak odpowiadający danemu kodowi całkowitemu

def alphabet_range(start="A", end="z", step=1):
    return (chr(x) for x in range(ord(start), ord(end), step))
# alphabet_range ("a", "f", 1)
list(alphabet_range(end="N"))

# to samo tylko, skopiowane z chatu
def alphabet_range(start="A", end="z", step=1):
    return (chr(x) for x in range(ord(start), ord(end), step))


#alphabet_range("a", "f", 1)

list(alphabet_range(end="M"))




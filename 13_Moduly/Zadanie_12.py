# stworzyc słownik { 'first': funkcja1, 'second': funkcja2 },
# wczytać przez sys.argv klucz, wywołać funkcję
import sys


def f1(n="OK"):
    """
    ta funckja wpisuje 'OK'
    return: OK
    """
    print(n)

def f2(x="NOK"):
    print(x)

s= {'f1':f1, 'f2':f2}
if __name__ == '__main__':
    print(sys.argv)
    klucz = (sys.argv[1])
    funkcja = s[klucz]
    funkcja()
    # funkcja() wywyołuje funkcję
    print(klucz)

# to zadanie służy do tego, że w temrinalu wyskauje rozwiązanie


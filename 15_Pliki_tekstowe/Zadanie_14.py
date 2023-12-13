# Stwórz czytnik plików CSV bez użycia modułu CSV
#
# napisz skrypt który otworzy plik z danymi csv (nazwa podana z CLI)
# wypisze jego zawartość oddzielając pola tabulacją \t

import os
print(os.getcwd())
# tego nie trzeba


with open('data/foods.csv') as f:
    for l in f:
        dane = l.strip().split(',')
        print ("\t".join(dane))




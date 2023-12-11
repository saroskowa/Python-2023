s = 'Ala ma {0} kotów'.format(5)
s

'Ala ma ' + str(5) + ' kotów'

s = 'Ala ma {0} kot{1}'.format(5, 'ów')
s

s = 'Ala ma {0} kot{1}'.format(4, 'y')
s

f'Pi to jest mniej więcej {3.1415926:.3}'

for i in range(12):
    print(f'{i:2}')

for i in range(12):
    print(f'{i:02}')

from math import pi
pi

f'{pi:.3}'
f'{pi:.3f}'
f'{pi-3:.3f}'
f'{12:3d}'
f'{12:03d}'
f'{pi:<30.2f}'
f'{pi:>30.2f}'
f'{pi:->30.2f}'
f'{pi:^30.2f}'
f'{"-"*10}HELLO{"-"*10}'
f'{"HELLO":-^25s}'

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

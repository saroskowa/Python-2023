a = 3

a == 3
a != 3

a > 2
a < 3
a >= 3
a <= 3

a = int(input("podaj liczbe"))
b = a/10
c = a//10
i = a+b
if(i % 7== 0 and a % 2== 0):
    print("liczba jest dobra")
else:
    print("liczba jest zla")
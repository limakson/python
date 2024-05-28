liczby = []

# dodaj liczby do listy liczby
with open("liczby.txt") as f:
    for liczba in f.readlines():
        liczby.append(int(liczba))

jeden = 0
dwa = 0
trzy = 0
ilosc = 0

for liczba in liczby:
    # print(liczba)

    temp_liczba = liczba

    while temp_liczba > 0:
        if temp_liczba % 10 == 1:
            jeden += 1
        elif temp_liczba % 10 == 2:
            dwa += 1
        elif temp_liczba % 10 == 3:
            trzy += 1
        else:
            continue

        temp_liczba //= 10

    temp_liczba2 = liczba
    suma = 0

    if liczba % 2 == 0:
        while temp_liczba2 > 0:
            suma += temp_liczba2 % 10
            temp_liczba2 //= 10
        if suma > 5:
            ilosc += 1


print("a")
print("liczba jedynek",jeden)
print("liczba dwójek",dwa)
print("liczba trójek",trzy)

print("b")
print(ilosc)

print("c")




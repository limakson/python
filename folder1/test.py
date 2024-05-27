liczby = []

with open("liczby.txt") as f:
    for liczba in f.readlines():
        liczby.append(int(liczba))

print(liczby)

suma=0
niepa=0
for liczba in liczby:
    if (liczba>100):
        suma=suma+liczba

    if (liczba%2==1):
        niepa=niepa + 1

print("suma:", suma)
print("nieparzystych jest", niepa)

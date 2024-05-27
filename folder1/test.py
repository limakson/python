liczby = []

with open("liczby.txt") as f:
    for liczba in f.readlines():
        liczby.append(int(liczba))

print(liczby)

# limak debil

text = "Kocham piwo \n"
slowo = ""
liczba = 0
for i in range(0,len(text)):

    # if text[i] == "o":
    slowo += text[i]

    if text[i] == " " or text[i] == "\n":
        print(slowo)
        if slowo == "piwo " or slowo == "piwo" or slowo == "Piwo" or slowo == "Piwo ":
            liczba += 1
        slowo = ""

print(liczba)

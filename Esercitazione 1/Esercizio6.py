coniugato = input("Coniugato?\n")
reddito = int(input("Reddito?\n"))
if coniugato == "si":
    if 0 < reddito < 10000:
        print("Tasse dovute = 0€")
    elif 10000 < reddito < 30000:
        print("Tasse dovute = ", (reddito - 10000)*0.12)
    else:
        print("Tasse dovute = ", (reddito - 30000)*0.3)
elif coniugato == "no":
    if 0 < reddito < 10000:
        print("Tasse dovute = 0€")
    elif 10000 < reddito < 30000:
        print("Tasse dovute = ", (reddito - 10000) * 0.15)
    else:
        print("Tasse dovute = ", (reddito - 30000) * 0.35)
else:
    print("Errore")


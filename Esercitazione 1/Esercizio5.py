day = int(input("Inserire il giorno\n"))
month = int(input("Inserire il mese\n"))

if (month in [1, 2]) or (month == 3 and day <= 21) or (month == 12 and day >= 22):
    print("Inverno")
elif (month in [4, 5]) or (month == 3 and day > 21) or (month == 6 and day <= 20):
    print("Primavera")
elif (month in [7, 8]) or (month == 6 and day > 20) or (month == 9 and day <= 22):
    print("Estate")
elif (month in [10, 11]) or (month == 9 and day > 22) or (month == 12 and day <= 21):
    print("Autunno")
else:
    print("I valori inseriti non sono corretti")

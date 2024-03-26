ls = []
for i in range(4):
    ls.append(int(input("Inserisci un numero ")))
if ls[0] < ls[1] < ls[2] < ls[3]:
    print("Sequenza strettamente crescente")
elif ls[0] > ls[1] > ls[2] > ls[3]:
    print("Sequenza strettamente decrescente")
else:
    print("Sequenza mista")
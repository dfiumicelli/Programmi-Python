num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ricercato = 27
trovato = False
for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if num[i] * num[j] == ricercato:
            trovato = True
        if trovato:
            break
if trovato:
    print("Trovato")
else:
    print("Non trovato")

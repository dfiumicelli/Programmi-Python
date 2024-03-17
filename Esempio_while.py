correct_answer = False
count = 0
while not correct_answer and count < 3:
    user_answer = input("Qual è la Capitale di Italia?\n")
    if user_answer == "Roma":
        correct_answer = True
        print("Riposta Corretta")
    else:
        print("Ritenta")
        count += 1
if not correct_answer:
    print("Hai sbagliato per tre volte")

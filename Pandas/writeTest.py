with open("test.csv", "w") as f:
    a = 5
    b = 6
    c = a + b
    f.write(str(c) + "\n")
f.close()

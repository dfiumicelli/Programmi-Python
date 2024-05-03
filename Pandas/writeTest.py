with open("test_mio.csv", "w") as f:
    a = 5
    b = 6
    c = a + b
    f.write(str(c) + "\n")
f.close()

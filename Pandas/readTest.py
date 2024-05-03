with open("test.csv", "r") as f:
    content = f.read()
    print(content)
f.close()

# oppure

with open("test.csv", "r") as f:
    content = f.readlines()
    for line in content:
        print(line)
f.close()

# oppure con iterator

with open("test.csv", "r") as f:
    for line in f:
        print(line)
f.close()
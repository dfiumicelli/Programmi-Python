def custom_func(first, second):
    first = first**2
    return first + second


x = 2
y = 4

print("Passaggio senza nome ordine x, y ", custom_func(x, y))
print("Passaggio senza nome ordine y, x ", custom_func(y, x))
print("Passaggio con nome ordine x, y ", custom_func(first=x, second=y))
print("Passaggio con nome ordine y, x ", custom_func(second=y, first=x))


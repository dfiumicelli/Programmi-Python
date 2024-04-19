import numpy as np

a = np.ones(shape=(3, 3))
b = np.ones(shape=(3, 3)) + 2
print("a+1", a+1)
print("a-2", a-2)
print("a+b", a+b)
print("a*b", a*b)  # non è il prodotto riga-colonna, ma solo il prodotto di ogni singolo elemento
# si possono fare operazioni elementwise solo tra ndarray della stessa dimensione
# si possono fare anche confronti booleani
print("a==b", a == b)
print("a > b", a > b)
print("a = b?", np.array_equal(a, b))

# si possono fare anche operazioni logiche

x = np.ones(shape=(3, 3), dtype=bool)
y = np.zeros(shape=(3, 3), dtype=bool)
print("x", x)
print("y", y)
print("x or y", np.logical_or(x, y))
print("x and y", np.logical_and(x, y))

# si possono usare le Universal Function di numpy che anch'esse funzioni elementwise
print("a*b", np.multiply(a, b))
print("a+b", np.add(a, b))
print("cos(a)", np.cos(a))
print("sin(a)", np.sin(a))


# somma su ogni riga
c = np.random.normal(size=(3, 3))
print("somma di ogni riga", np.add(a, axis=0))
print("somma di ogni colonna", np.add(a, axis=1))

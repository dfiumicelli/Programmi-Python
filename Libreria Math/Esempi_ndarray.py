import numpy as np

# a = np.zeros(shape=(3, 3))
# print(a.shape, a.size, a[0].size)
b = np.arange(9)
c = np.reshape(b, (3, 3))
# print(c)
d = np.ravel(c)
# print(d)

# come si fa a iterare su un ndarray?

a = np.random.normal(size=(2, 2, 3))
# print(a)
# for element in a.ravel():
    # print(element)
# oppure
for n in a:
    for m in n:
        print(m, "\n")
def f_incr_and_app(ls, b):
    print("id di b nel local namespace", id(b))
    b = b+1
    print("id di b  dopo l'incremento nel local namespace", id(b))
    ls.append(b)
    print("id di ls nel local namespace", id(ls))


x = 13
L = [10, 11, 12]
print("id di x nel global namespace", id(x))
print("id di L nel global namespace", id(L))
print("Valore di L: ", L)
f_incr_and_app(L, x)
print("Valore di x dopo la funzione: ", x)
print("id di L nel global namespace dopo la funzione: ", id(L))
print("Valore di L dopo la funzione ", L)
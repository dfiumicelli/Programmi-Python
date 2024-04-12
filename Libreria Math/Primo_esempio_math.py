import math
import os
import statistics
from myModule import my_function


print(math.cos(math.pi))
print(os.path.join("parent_dir", "child_dir"))  #si usa per unire due directory in modo crossplatform
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [6, 7, 8, 9, 10, 11, 12, 13, 14]
print(statistics.mean(x))
print(statistics.stdev(x))
print(statistics.covariance(x, y))

z = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(statistics.covariance(x, z))
print(statistics.covariance(y, z))
print(my_function(1, 2))  #ho importato il modulo e quindi posso usare la funzione che è in quel modulo.

#ti amo <3

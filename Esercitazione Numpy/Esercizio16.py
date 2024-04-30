import numpy as np

x = np.random.rand(2, 4)
x_mean = x.mean(axis=1, keepdims=True)  # altrimenti si perderebbe una dimensione, tirando fuori un'eccezione quando fa il broadcasting
y = x-x_mean
print(x)
print(y)

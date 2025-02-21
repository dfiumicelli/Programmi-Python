import numpy as np
from matplotlib import pyplot as plt


class Espressione:
    def __init__(self, M1, M2, alpha):
        self.__alpha = alpha
        a = np.random.normal(size=(3,3), loc=alpha)
        b = np.random.normal(size=(3,3), loc=alpha)
        A = M1@a
        B = M2@b
        self.__A = A
        self.__B = B

    def stampa(self):
        print("Alpha\n", self.__alpha)
        print("A\n", self.__A)
        print("B\n", self.__B)

    def step(self,k):
        u = np.zeros(shape=(3,k))
        u[0,:] = np.arange(0,k)
        for j in range(0,k):
            u[1,j] = (j+1)**2
            u[2,j] = j%2
        return u

    def response(self,k,x):
        u = self.step(k)
        X = np.zeros((3, k+1))
        X[:,0] = x
        for i in range(0,k):
            X[:,i+1] = self.__A@X[:,i] + self.__B@u[:,i]

        return X

    def plot(self,k,x):
        X = self.response(k,x)
        fig, ax = plt.subplots(3)
        ax[0].plot(range(X.shape[1]),X[0,:])
        ax[1].plot(range(X.shape[1]),X[1,:])
        ax[2].plot(range(X.shape[1]),X[2,:])
        plt.show()

    def func(self, c):
        D = np.zeros(self.__A.shape)
        for i in range(0,self.__A.shape[0]):
            for j in range(0,self.__A.shape[1]):
                if i==j:
                    D[i,j] = self.__A[i,j] + self.__B[i,j]
        D[D>c]+=3
        print(D)

M1 = np.array([[-0.2, -0.1, -0.3],[0.1, 0., 0.2], [0., 0.1, 0.1]])
M2 = np.array([[-0., -0.1, -0.], [0.1, 0.1, 0.1], [0., 0.1, 0.2]])
x = np.array([[1., 1., 1.]])
alpha = 2
k = 50
e = Espressione(M1, M2, alpha)

print(e.response(k,x))
e.plot(k,x)
e.func(0.0)
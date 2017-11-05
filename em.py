import numpy as np
import matplotlib.pyplot as plt
import math
import copy

#.......
def init_data(sigma, u1, u2, k, n):
    global X, u, Expectations
    X = np.zeros( (1, n) )
    u = np.random.random(2)
    Expectations = np.zeros( (n, k) )
    for i in range(n):
        if np.random.random(1) > 0.5:
            X[0, i] = np.random.normal() * sigma + u1
        else:
            X[0, i] = np.random.normal() * sigma + u2
   # print(X)

def e_step(sigma, k, n):
    global Expectations, u, X
    for i in range(n):
        Denom = 0
        for j in range(k):
            Denom += math.exp((-1/(2*(float(sigma**2))))*(float(X[0,i]-u[j]))**2)
        for j in range(k):
            Numer = math.exp((-1/(2*(float(sigma**2))))*(float(X[0,i]-u[j]))**2)
            Expectations[i, j] = Numer/Denom

def m_step(k, n):
    global Expectations, X
    for j in range(k):
        Number = 0
        Denom = 0
        for i in range(n):
            Number  += Expectations[i, j] * X[0, i]
            Denom += Expectations[i, j]
        u[j] = Number/Denom

def run(sigma, u1, u2, k, n, iter_num, Epsilon):
    init_data(sigma, u1, u2, k, n)
    print('初始u', u)
    for i in range(iter_num):
        old_u = copy.deepcopy(u)
        e_step(sigma, k, n)
        m_step(k, n)
        print(i, u)
        if sum( abs(u-old_u) ) < Epsilon:
            break

if __name__ == '__main__':
    run(6, 10, 20, 2, 1000, 100, 0.0001)
    plt.hist(X[0, :], 50)
    plt.show()
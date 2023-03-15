import numpy as np
import matplotlib.pyplot as plt

def maxexpred(n_act):
    s = []

    for i in range(10000):
        s.append(max(np.random.normal(0, 1, n_act)))
        
    return np.mean(s)

x = range(1, 30)
y = [maxexpred(i) for i in x]
plt.plot(x, y)
plt.savefig('img.png')
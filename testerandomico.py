import math 
import random
import numpy as np
import matplotlib.pyplot as plt

random.seed()

Prob = 1/60

n = 10000
a = np.zeros(n)

for i in range(n):

    if random.random() <= Prob:
        a[i] = 1
    
    print(a[i])

soma = sum(a)
print(soma)

plt.hist(a, density=True, bins=30)  # density=False would make counts
plt.ylabel('Probability')
plt.xlabel('Data')
plt.show()
# Übung 1: 
import numpy as np 

a = np.array(range(1,13))
a1 = a.reshape(3,2,2)
a1

# Übung 2: 
a1.ndim # Anzahl der Dimensionen 
a1.shape
a1.size
a1.dtype

# Übung 3 - Excercise 10: 
M = np.eye(5, dtype = "int")
M[0:2,3:5] = 3
M[3:5, 0:2] = 2 
M

# Übung 4 - Excercise 11:  
data = np.arange(1,11)
D = np.tile(data,10).reshape(10,10)
print(D.sum(axis = 0))
print(D.mean(axis = 1 ))


# Übung 5 - Excercise 12: 

M = np.array([3,2,1,4]).reshape(2, 2)

M_inv = np.linalg.inv(M)

I = np.matmul(M_inv, M)

A = np.array([7, 5, -3, 3, 
              -5, 2, 5, 3, -7]).reshape(3, 3)

r = np.array([16, -8, 0]).reshape(3, 1)

A_inv = np.linalg.inv(A)

b = np.matmul(A_inv, r)

# Übung 6 - Excercise 13: 
from math import log10
import numpy as np

x = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]

x_log10 = [log10(k) for k in x]

x_log10_array = np.log10(x)

# Übung 7 - Excercise 14: 
y = [2, 3, 8, 4, 10, 1, 9, 5, 1, 0]

y_std = np.sqrt(1/len(y) * sum((y - np.mean(y))**2))

'''Program to find L and U matrix using LU decomposition.
Developed by: Rohith S
RegisterNumber: 25008317
'''
import numpy as np
from scipy.linalg import lu
a = np.array(eval(input()))
_,L,U = lu(a)
print(L)
print(U)
# LU Decomposition 

## AIM:
To write a program to find the LU Decomposition of a matrix.

## Equipments Required:
1. Hardware – PCs
2. Anaconda – Python 3.7 Installation / Moodle-Code Runner

## Algorithm
### Step 1: 
Import the required Python libraries (numpy and scipy.linalg).
### Step 2: 
Get the input matrix from the user (or define it in the program).
### Step 3: 
Use the LU decomposition function (lu for matrices or lu_factor and lu_solve for solving equations).
### Step 4: 
Display the L and U matrices and/or the solution for the system of linear equations.
## Program:
### Developed by: Rohith S
### RegisterNumber: 25008317
(i) To find the L and U matrix
```
import numpy as np
from scipy.linalg import lu
a = np.array(eval(input()))
_,L,U = lu(a)
print(L)
print(U)
```
(ii) To find the LU Decomposition of a matrix
```
# To print X matrix (solution to the equations)
import numpy as np
from scipy.linalg import lu_factor,lu_solve
a = np.array([[3,2,7],[2,3,1],[3,4,1]])
b = np.array([4,5,7])
lp = lu_factor(a)
x= lu_solve(lp ,b)
print(x)
```

## Output:
<img width="974" height="330" alt="image" src="https://github.com/user-attachments/assets/2d1d64bb-f5e9-4289-a355-0b5708746afa" />

<img width="748" height="139" alt="image" src="https://github.com/user-attachments/assets/1eb7c814-a07b-4245-b12f-385aa31b9fd8" />


## Result:
Thus the program to find the LU Decomposition of a matrix is written and verified using python programming.
on

import numpy as np
"""arr=np.array([1,2,3,4,5])
arr2=np.array([10,20,30,40,50])
print(arr+arr2)
print(arr*2)
print(arr**2)
print(np.mean(arr))
print(np.sum(arr))
matrix=np.array([[1,2,3],
                [4,5,6],
                [7,8,9]
])
print(matrix)
print(matrix.shape)
print(matrix[0])
print(matrix[1,2])
print(matrix*2)
print(matrix.sum())
print(matrix.mean())
print(matrix.sum(axis=0))
print(matrix.sum(axis=1))"""
A=np.array([[1,2],
           [3,4]])
B=np.array([[5,6],
           [7,8]])
print(np.dot(A, B))
print(A.T)
print(np.linalg.inv(A))
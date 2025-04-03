#shape and reshaping of array

import numpy as np

#create 1D array
np1 = np.array([1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 11])
print(np1)
print(np1.shape)

print('\n')
#create 2D array
np2 = np.array([[1, 2, 3], [4, 4, 5]])
print(np2)
print(np2.shape)

print('\n')
#reshape into a 2D array
np3 = np1.reshape(3, 4)
print(np3.base) #view of the original array
print(np3.shape)

print('\n')
#reshape into a 3D array
np4 = np1.reshape(3, 2, 2)
print(np4)
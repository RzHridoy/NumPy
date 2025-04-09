print("Beginning of the NumPY Course \n")

import numpy as np

list1 = [1, 2, 3, 4, 5]
print(list1)
print('\n')

np1 = np.array([[1, 2, 3],
               [2, 3, 2]])
print(np1)
print('\n')
print(np1.shape)
print('\n')
print(np1.ndim)
print('\n')
print(np1.itemsize)
print('\n')

#list does not allow multiplication
'''li2 = [2, 3]
li3 = [3, 4]
print(li2 * li3)
print('\n')'''

#numpy matrix allows multiplication
np2 = np.array([2, 3])
np3 = np.array([3, 4])
print(np2 * np3)
#iterating and enumerating

import numpy as np

np1 = np.array([[[1, 2, 3], [2, 3, 4], [3, 6, 8]]])
print(np1)
print(np1.shape)
print(np1.ndim)

print('\n')
#iter
for x in np.nditer(np1):
    print(x)
    
print('\n')
#enumerate
for idx, x in np.ndenumerate(np1):
    print(idx, x)
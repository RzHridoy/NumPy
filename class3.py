#view and copy of an array
import numpy as np

np1 = np.array([1, 2, 3, 4])
print(f"Original NP1 is {np1}")

#create a view
np2 = np1.view()
print(f"Original NP2 is {np2}")

#create view after changing np1 then np2 array
'''np1[2] = 5
print(f"Change NP1 is {np1}")
print(f"Original NP2 is {np2}")'''

np2[0] = 0
print(f"Original NP1 is {np1}")
print(f"Change NP2 is {np2}")
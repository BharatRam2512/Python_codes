import numpy as np
def slicing(arr):
    return arr[:2,-2:]
arr=np.arange(9).reshape(3,3)
print("before slicing: \n", arr)
print("after slicing: \n", slicing(arr))
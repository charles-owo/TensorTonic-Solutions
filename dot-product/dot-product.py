import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    arr_1 = np.array(x)
    arr_2 = np.array(y)

    return float(np.dot(arr_1,arr_2))
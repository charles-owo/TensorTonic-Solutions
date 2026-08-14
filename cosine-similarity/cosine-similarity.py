import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    arr_1 = np.array(a)
    arr_2 = np.array(b)
    dot_product = np.dot(arr_1,arr_2)
    mag_a = np.linalg.norm(arr_1)
    mag_b = np.linalg.norm(arr_2)

    if mag_a == 0 or mag_b == 0 :
        ans = float(0)
    else :
        ans = dot_product/(mag_a * mag_b)
    return ans
import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    e = np.exp(x - np.max(x))
    is_two_dim = (e.ndim == 2)
    return e / np.sum(e, axis=1*is_two_dim, keepdims=is_two_dim)
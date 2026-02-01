import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    # Write code here
    return np.tanh(np.transpose(Wx) @ x_t + np.transpose(Wh) @ h_prev + b)

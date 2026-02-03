import numpy as np

def q_learning_update(Q, s, a, r, s_next, alpha, gamma):
    """
    Returns: updated Q-table Q_new
    """
    # Write code here
    Q = np.array(Q)
    curQ = Q[s][a]
    a_next = np.argmax(Q[s_next])
    maxQ = Q[s_next][a_next]
    Q[s][a] = Q[s][a] + alpha * (r + gamma * maxQ - curQ)
    return Q
    
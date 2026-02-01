def sarsa_update(q_table, state, action, reward, next_state, next_action, alpha, gamma):
    """
    Perform one SARSA update and return the updated Q-table.
    """
    # Write code here

    curr_value = q_table[state][action]
    next_value = q_table[next_state][next_action]
    delta = reward + gamma * next_value - curr_value

    q_table[state][action] = curr_value + alpha * delta
    return q_table
    
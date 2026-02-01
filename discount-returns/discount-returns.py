def discount_returns(rewards, gamma):
    """
    Compute the discounted return at every timestep.
    """
    # Write code here
    for i in range(len(rewards) - 1, 0, -1):
        rewards[i - 1] += rewards[i] * gamma
    return rewards
    
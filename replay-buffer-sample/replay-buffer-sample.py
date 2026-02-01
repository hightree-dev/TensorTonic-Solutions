def replay_buffer_sample(buffer, batch_size, seed):
    """
    Sample a batch of transitions from the replay buffer.
    """
    # Write code here
    random.seed(seed)
    return random.sample(buffer, batch_size)
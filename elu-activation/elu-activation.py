def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    e = []

    for num in x:
        if num > 0:
            e.append(num)
        else:
            e.append(alpha * (math.exp(num) - 1))
    
    return e
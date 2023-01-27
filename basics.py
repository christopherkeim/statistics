#Basic statistics functions.

def average(vector):
    """Returns the average or mean of an input numerical vector."""
    sum = 0.0
    for value in vector:
        sum += float(value)
    average = sum / len(vector)
    return average
    
def variance(vector):
    """Returns the variance of an input numerical vector."""
    avg = sum(vector) / len(vector)
    var_sum = 0.0
    for value in vector:
        var_sum += (float(value) - avg) ** 2
    #Sample variance is N - 1, typically used in sciences when dealing with smaller sample sizes.
    variance = var_sum / (len(vector) - 1)
    return variance
    
def standard_deviation(vector):
    """Returns the standard deviation of an input numerical vector."""
    var = variance(vector)
    sd = float(var ** 0.5)
    return sd

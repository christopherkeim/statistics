def normal_curve(vector, value):
    """Returns the output of a normal curve function constructed from the mean and SD of a given vector of samples for a
        passed in input value.
    """
    avg = average(vector)
    var = variance(vector)
    sd = standard_deviation(vector)
    weight = 1 / (sd * ((2 * math.pi) ** 0.5))
    dist = value - avg
    e = math.e ** -((dist ** 2) / (2 * var))
    gaussian = weight * e
    return gaussian

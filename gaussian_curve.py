import math
from basics import average, variance, standard_deviation

def normal_curve(vector, domain, step):
    """Returns the instantiated function mapping for the normal curve generated from the input numerical vector in a given
        domain and point resolution step.
    """
    avg = average(vector)
    var = variance(vector)
    sd = standard_deviation(vector)
    weight = 1 / (sd * ((2 * math.pi) ** 0.5))
    gaussian = {}
    for i in range(domain[0], domain[1], step):
        dist = i - avg
        e = math.e ** -((dist ** 2) / (2 * var))
        gaussian[i] = weight * e
    return gaussian

def euclidean(self, sample1, sample2):
    """
    Calculates the Euclidean distance between two passed in vectors, where d = ((Δx)**2 + Δy**2 + Δz**2 + ...))**0.5.
    """
    sum_sq = 0.0
    for i in range(len(sample1)):
        sum_sq += (sample1[i] - sample2[i]) ** 2
    distance = sum_sq ** 0.5
    return distance

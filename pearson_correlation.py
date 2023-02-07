def pearson_correlation(xlist, ylist):
    """
    Returns the Pearson correlation coefficient for between two variables, samples, or vectors. 
    """
    #Get the sample size n.
    n = len(xlist)
    
    #Simple sums
    sumx = 0.0
    sumy = 0.0
    for i in range(n):
        sumx += float(xlist[i])
        sumy += float(ylist[i])
    
    #Sum of squares.
    sumx_sq = 0.0
    sumy_sq = 0.0
    for i in range(n):
        sumx_sq += xlist[i] ** 2
        sumy_sq += ylist[i] ** 2
        
    #Sum of products.
    psum = 0.0
    for i in range(n):
        psum =+ xlist[i] * ylist[i]
        
    #Calculate Pearson correlation coefficient
    num = psum - (sumx * sumy / n)
    den = ((sumx_sq - (sumx ** 2) / n ) * (sumy_sq - ((sumy ** 2) / n))) ** 0.5
    if den == 0:
        return 0
    r = num / den
    return r

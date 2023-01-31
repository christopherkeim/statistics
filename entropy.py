from math import log

def entropy(samples):
	"""
	Takes a 2d nested list of samples, extracts a frequency count of the output variable values, them calculates the entropy for this group
    of samples as entropy = Σ pi * log2(pi)   [from i=1 to n]
	"""
	#log2 function
	def log2(x):
		return log(x) / log(2)
			
	#store the frequency counts of the output variable values in this group of samples in a dictionary
	counts = self.outputValueCounts(samples)
		
	#calculate the entropy
	entropy = 0.0
		
	for value in counts:
		p = float(counts[value] / len(samples))
		entropy -= p * log2(p)
			
	return entropy

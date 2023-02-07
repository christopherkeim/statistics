from math import log

def entropy(samples):
	"""
	Takes a vector of samples, extracts a frequency count of the categorical variable values, then calculates the entropy for this group
	of samples as entropy = Σ pi * log2(pi)   [from i=1 to n]
	"""
	#log2 function
	def log2(x):
		return log(x) / log(2)
	
	def get_value_counts(vec):
		val_counts = {}
		for val in vec:
			if val not in val_counts:
				val_counts[val] = 0
			val_counts[val] += 1
		return val_counts
				
	#store the frequency counts of the output variable values in this group of samples in a dictionary
	counts = get_value_counts(samples)
		
	#calculate the entropy
	entropy = 0.0
		
	for value in counts:
		p = float(counts[value] / len(samples))
		entropy -= p * log2(p)
			
	return entropy

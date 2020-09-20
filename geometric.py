 
from math import log2 as log


def prob(n, p):
	return (1 - p) ** (n - 1) * p


def infoMeasure(n, p):
	return -log(prob(n, p))


def sumProb(N, p):
	'''
	Returns the CDF of Geometric distribution
		
		Parameters:
			N (int): number of trials
			p (float): success probability
		Returns:
			cdf (float): CDF of Geometric distribution w.r.t N
	'''

	return 1 - (1 - p) ** N


def approxEntropy(N, p):
	'''
	Returns the approximate Entropy according to Geometric information 
	source. Converge when N large.
	
		For example with p = 0.5
			Ent = 1.9 when N = 7
			Ent = 1.82 when N = 10
		=> Ent converge to 2
		Parameters:
			N (int): number of trials
			p (float): success probability
		Returns:
			Ent (float): accumulate Entropy to N trials.
	'''
	
	Ent = 0
	for k in range(1, N + 1):
		Pr = prob(k, p)
		I = infoMeasure(k, p)
		Ent += Pr * I
	 return Ent 
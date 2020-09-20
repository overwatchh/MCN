import operator as op
from functools import reduce
from math import log2 as log


def nCr(n, r):
	r = min(r, n-r)
	numer = reduce(op.mul, range(n, n-r, -1), 1)
	denom = reduce(op.mul, range(1, r+1), 1)
	return numer // denom


def prob(n, p, N):	
	return nCr(N, n) * p ** n * (1 - p) ** (N - n)


def infoMeasure(n, p, N):
	return -log(prob(n, p, N))


def sumProb(N, p):
	'''
	Returns sum of probs of Binomial info. source according to
		N (int): number of trials
		p (float): success probability for each trial
	'''

	s = 0

	for k in range(0, N + 1):
		s += prob(k, p, N)

	return s


def approxEntropy(N, p):
	'''
	Returns approximate Entropy of Binomial info. source according to
		N (int): number of trials
		p (float): succes probability for each trial
	For example with p = 0.5
		N = 2      H = 1.5
		N = 3	   H = 1.811
		N = 4      H = 2.03
	'''

	Ent = 0
	
	for k in range(0, N + 1):
		Pr = prob(k, p, N)
		I = infoMeasure(k, p, N)
		Ent += Pr * I
	
	return Ent
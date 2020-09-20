import operator as op
from functools import reduce
from math import log2 as log


def nCr(n, r):
	r = min(r, n - r)
	numer = reduce(op.mul, range(n, n - r, -1), 1)
	denom = reduce(op.mul, range(1, r + 1), 1)

	return numer // denom


def prob(n, p, r):
	return nCr(n - 1, n - r) * p ** r * (1 - p) ** (n - r)


def infoMeasure(n, p, r):
	return -log(prob(n, p, r))


def sumProb(N, p, r):
	'''
	Returns accumulate probability of Negative binominal info. source according to
		N (int): number of trials
		p (float): succuess probabilitty in each experiment
		r (int): number of successes until the experiment is stopped
	'''

	s = 0
	for r_ in range(r, N + 1):
		s += prob(r_, p, r)

	return s


def approxEntropy(N, p, r):
	'''
	Returns approximate Entropy of Negative binominal info. source according to
		N (int): number of trials
		p (float): success probability in each experiment
		r (int): number of successes until the experiment is stopped
	For example p = 0.5, r = 5 and N = 10
		H = 1.96
	'''

	Ent = 0
	for k in range(r, N + 1):
		Pr = prob(k, p, r)
		I = infoMeasure(k, p, r)
		Ent += Pr * I
	
	return Ent
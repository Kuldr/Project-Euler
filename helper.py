from typing import Dict, List
from unittest import result

def primeFactors(toFactor: int) -> Dict[int, int]:
	from collections import defaultdict

	current = 2
	primeFactors = defaultdict(lambda: 0)
	while current < toFactor:
		if toFactor % current == 0:
			primeFactors[current] += 1
			toFactor //= current
		else:
			current += 1
	
	primeFactors[current] += 1

	return primeFactors


def isPrime(n: int) -> bool:
	if n <= 1:
		return False
	elif n == 2:
		return True

	from math import sqrt
	sqrtN = int(sqrt(n)) + 1

	if n % 2 == 0:
		return False
	for candidate in range(3, sqrtN, 2):
		if n % candidate == 0:
			return False
	return True

def primeSieve(maxValue: int) -> List[int]:
	from math import sqrt, ceil
	candidates = {num: True for num in range(3, maxValue+1, 2)}

	for i in range(3, ceil(sqrt(maxValue)), 2):
		if candidates[i] == True:
			for j in range(i**2, maxValue+1, i):
					candidates[j] = False

	return [2] + [k for k, v in candidates.items() if v == True]

def primeGenerator() -> int:
	from math import sqrt

	primeList = [2]
	yield 2
	candidate = 3
	while True:
		primeFound = True
		sqrtCandidate = int(sqrt(candidate)) + 1
		for prime in primeList:
			if prime > sqrtCandidate:
				break
			if candidate % prime == 0:
				primeFound = False
				break
		
		if primeFound:
			primeList.append(candidate)
			yield candidate
		candidate += 2

def factors(n: int) -> List[int]:
	from math import sqrt
	factorsList = set([n])
	for i in range(1, int(sqrt(n))+1):
		if n % i == 0:
			factorsList.add(i)
			factorsList.add(n//i)

	return factorsList
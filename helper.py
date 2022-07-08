from typing import Dict, List

def primeFactors(toFactor: int) -> Dict[int, int]:
	current = 2
	primeFactors = []
	while current < toFactor:
		if toFactor % current == 0:
			primeFactors.append(current)
			toFactor //= current
		else:
			current += 1
	if current > 1:
		primeFactors.append(current)
		
	# Turn into dictionary with exponents
	return {prime:primeFactors.count(prime) for prime in set(primeFactors)}

def isPrime(n: int) -> bool:
	if n <= 1:
		return False
	elif n == 2:
		return True

	from math import sqrt
	sqrtN = int(sqrt(n)) + 1

	for candidate in range(3, sqrtN, 2):
		if n % candidate == 0:
			return False
	return True

def primeSieve(maxValue: int) -> List[int]:
	candidates = {num: True for num in range(3, maxValue+1, 2)}

	for i in range(3, int(maxValue**0.5), 2):
		if candidates[i] == True:
			j = i ** 2
			while j < maxValue:
				if j in candidates:
					candidates[j] = False
				j += i

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
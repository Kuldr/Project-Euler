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
	
	from math import sqrt
	sqrtN = int(sqrt(n)) + 1

	for candidate in range(2, sqrtN):
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

def factors(n: int) -> List[int]:
	factorsList = [n]
	for i in range(1, n//2+1):
		if n % i == 0:
			factorsList.append(i)

	return factorsList
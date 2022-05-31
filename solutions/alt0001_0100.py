def p0007Filter() -> int:
	"""10001st Prime Number"""
	# 104743
	primesFound = 0
	candidate = 1
	goal = 10001

	from helper import isPrime

	while primesFound < goal:
		candidate += 1
		if isPrime(candidate):
			primesFound += 1
		
	return candidate

def p0007ContinuousSieve() -> int:
	"""10001st Prime Number"""
	# 104743

	primeList = [2, 3, 5, 7, 11, 13]
	goal = 10001
	candidate = 15
	while len(primeList) < goal:
		primeFound = False
		while not primeFound:
			primeFound = True
			for prime in primeList:
				if candidate % prime == 0:
					primeFound = False
					break
			
			if primeFound:
				primeList.append(candidate)
			candidate += 2
	
	return primeList[-1]

def p0010Filter() -> int:
	"""Find the sum of all the primes below two million"""
	# 142913828922

	target = 2_000_000

	from helper import isPrime
	primesBelow = filter(isPrime, range(target))

	return sum(primesBelow)
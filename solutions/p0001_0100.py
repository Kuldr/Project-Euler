def p0001() -> int:
	"""Sum of multiples of 3 or 5 below 1000"""
	# 233168
	return sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])

def p0002() -> int:
	"""Even valued fibonacci terms bellow 4 million"""
	# 4613732
	fibs = [1,2]
	while (next := fibs[-1] + fibs[-2]) < 4_000_000:
		fibs.append(next)
	return sum([x for x in fibs if x % 2 == 0])

def p0003() -> int:
	"""Largest Prime Factor of 600851475143"""
	# 6857
	toFactor = 600851475143
	from helper import primeFactors
			
	return max(primeFactors(toFactor))

def p0004() -> int:
	"""Largest Palindrome as the product of 3 digit numbers"""
	# 906609
	from itertools import combinations
	threeDigitsCombos = combinations(range(100,1000), 2)
	products = map(lambda x: x[0]*x[1], threeDigitsCombos)
	palandromes = [x for x in products if str(x) == str(x)[::-1]]
	return max(palandromes)

def p0005() -> int:
	"""Smallest number that is a multiple of the numbers from 1 to 20"""
	# 232792560
	from helper import primeFactors
	from collections import defaultdict
	factors = defaultdict(lambda: 1)
	for i in range(1,21):
		currentFactors = primeFactors(i)
		for prime, exponent in currentFactors.items():
			if factors[prime] < exponent:
				factors[prime] = exponent

	ans = 1
	for prime, exponent in factors.items():
		ans *= prime ** exponent

	return ans

def p0006() -> int:
	"""Difference between the sum of the squares of numbers 1 to 100 and the square of the sum"""
	# 25164150
	sumSqaures = sum([x**2 for x in range(101)])
	squareSum  = sum(range(101))**2
	return squareSum 

def p0007() -> int:
	"""10001st Prime Number"""
	# 104743
	from math import log
	goal = 10001
	upperBound = round(goal * (log(goal) + log(log(goal))))

	from helper import primeSieve
	return primeSieve(upperBound)[goal-1]

def p0008() -> int:
	"""13 adjacent digits in the 1000-digit number that have the greatest product"""
	# 23514624000
	num1000 = ("73167176531330624919225119674426574742355349194934"
				"96983520312774506326239578318016984801869478851843"
				"85861560789112949495459501737958331952853208805511"
				"12540698747158523863050715693290963295227443043557"
				"66896648950445244523161731856403098711121722383113"
				"62229893423380308135336276614282806444486645238749"
				"30358907296290491560440772390713810515859307960866"
				"70172427121883998797908792274921901699720888093776"
				"65727333001053367881220235421809751254540594752243"
				"52584907711670556013604839586446706324415722155397"
				"53697817977846174064955149290862569321978468622482"
				"83972241375657056057490261407972968652414535100474"
				"82166370484403199890008895243450658541227588666881"
				"16427171479924442928230863465674813919123162824586"
				"17866458359124566529476545682848912883142607690042"
				"24219022671055626321111109370544217506941658960408"
				"07198403850962455444362981230987879927244284909188"
				"84580156166097919133875499200524063689912560717606"
				"05886116467109405077541002256983155200055935729725"
				"71636269561882670428252483600823257530420752963450")

	num1000Digits = [int(c) for c in num1000]

	# This creates sublists of len < 13 at end but there result will be less than the last full 13
	sublists = [num1000Digits[n:n+13] for n in range(len(num1000Digits))]
 
	from math import prod

	results = map(prod, sublists)

	return max(results)

def p0009() -> int:
	"""abc | a<b<c and a+b+c = 1000 and a^2 + b^2 = c^2"""
	# 31875000

	from itertools import combinations
	combos = combinations(range(1000), 3)

	equal1000 = lambda t: sum(t) == 1000
	pythTriple = lambda t: t[0]**2 + t[1]**2 == t[2]**2
	combos = filter(equal1000, combos)
	combos = filter(pythTriple, combos)

	ans = next(combos)

	return ans[0] * ans[1] * ans[2]

def p0010() -> int:
	"""Find the sum of all the primes below two million"""
	# 142913828922

	target = 2_000_000

	from helper import primeSieve
	primesBelow = primeSieve(target)
	return sum(primesBelow)

def p0011() -> int:
	"""What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?"""
	# 70600674
	numGrid =  ("08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08\n"
				"49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00\n"
				"81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65\n"
				"52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91\n"
				"22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80\n"
				"24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50\n"
				"32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70\n"
				"67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21\n"
				"24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72\n"
				"21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95\n"
				"78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92\n"
				"16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57\n"
				"86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58\n"
				"19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40\n"
				"04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66\n"
				"88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69\n"
				"04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36\n"
				"20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16\n"
				"20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54\n"
				"01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48")

	# Parse Data
	coords = {}
	for y, row in enumerate(numGrid.split("\n")):
		for x, val in enumerate(row.split(" ")):
			coords[(x, y)] = int(val)
			
	startingCoords = coords.keys()
	maxProduct = 0

	def productInDir(coords, x, y, xDiff, yDiff):
		from math import prod
		return prod([coords[(x+xDiff*i, y+yDiff*i)] for i in range(4)])

	from itertools import product
	directions = list(product([-1, 0, +1], repeat=2))
	directions.remove((0, 0))
	
	for x, y in startingCoords:
		for xDiff, yDiff in directions:
			try:
				result = productInDir(coords, x, y, xDiff, yDiff)
			except KeyError:
				result = 0
			if result > maxProduct:
				maxProduct = result
	return maxProduct

def p0012() -> int:
	"""What is the value of the first triangle number to have over five hundred divisors?"""
	# 76576500

	def numFactors(n: int) -> int:
		from helper import primeFactors
		from math import prod
		return prod([v + 1 for v in primeFactors(n).values()])
	
	n = 1
	triangleN = 1
	while numFactors(triangleN) < 500:
		n += 1
		triangleN += n
		if n % 1000 == 0:
			print(n, triangleN)
		
	return triangleN

def p0013() -> int:
	"""Work out the first ten digits of the sum of the following one-hundred 50-digit numbers."""
	# 5537376230

	# File in data section
	f = open("solutions/data/p0013.txt", "r")
	numsStr = f.read()
	f.close()

	nums = [int(x) for x in numsStr.split("\n")]
	ans = sum(nums)

	return str(ans)[0:10]

def p0014() -> int:
	"""Collatz sequence; Which starting number, under one million, produces the longest chain?"""
	# 837799

	from functools import lru_cache
	@lru_cache(maxsize=None)
	def collatzLength(n: int) -> int:
		if n == 1:
			return 1
	
		if n % 2 == 0:
			return 1 + collatzLength(n//2)
		else:
			return 2 + collatzLength((3*n+1)/2)
		
	best = 0
	bestVal = 0
	for i in range(1, 1_000_000+1):
		if (collatzI := collatzLength(i)) > bestVal:
			bestVal = collatzI
			best = i

	return best

def p0015() -> int:
	"""How many lattice path routes are there through a 20×20 grid?"""
	# 137846528820
	goal = 20

	from functools import lru_cache
	@lru_cache(maxsize=None)
	def numPaths(x: int, y: int) -> int:
		if x < 0 or y < 0:
			return 0
		elif x == 0 and y == 0:
			return 1
		else:
			return numPaths(x-1, y) + numPaths(x, y-1)
	
	return numPaths(goal, goal)
	
def p0016() -> int:
	"""Sum of the digits of 2^1000"""
	# 1366

	num = 2 ** 1000
	return sum([int(x) for x in str(num)])

def p0019() -> int:
	"""Sundays that fell on the first of the month during the 20th century"""
	# 171

	from datetime import datetime
	from itertools import product
	
	sunday = 6

	years = list(range(1901, 2000+1))
	months = list(range(1,12+1))
	days = [1]

	dates = product(years, months, days)
	days = [datetime(*x).weekday() for x in dates]

	return days.count(sunday)

def p0020() -> int:
	"""Find the sum of the digits in the number 100!"""
	# 648

	from math import factorial
	num = factorial(100)
	digits = [int(d) for d in str(num)]

	return sum(digits)

def p0021() -> int:
	"""Evaluate the sum of all the amicable numbers under 10000"""
	# 31626

	target = 10_000

	from helper import factors
	from functools import cache
	@cache
	def sumProperFactors(n):
		ans = factors(n)
		ans.remove(n)
		return sum(ans)

	def amicable(n):
		sumA = sumProperFactors(n)
		sumB = sumProperFactors(sumA)
		if sumB == n and n != sumA:
			return True
		
	amicableCount = 0
	for x in range(target+1):
		if amicable(x):
			amicableCount += x
	return amicableCount

def p0022() -> int:
	"""What is the total of all the name scores in the file?"""
	# 871198282

	# File in data section
	f = open("solutions/data/p0022.txt", "r")
	fileStr = f.read()
	f.close()

	# Format data into sorted list
	fileStr = fileStr.translate({ord('"'): None})
	names = fileStr.split(",")
	names.sort()
	
	# Calculate scores
	totalScore = 0
	for i, name in enumerate(names):
		nameScore = sum([ord(c) - ord("A") + 1 for c in name])

		totalScore += nameScore * (i + 1)

	return totalScore
		

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
	"""13 adjacent digits in the 1000 digit number that have the greatest product"""
	# 23514624000
	
	# File in data section
	f = open("solutions/data/p0008.txt", "r")
	num1000 = f.read()
	num1000 = num1000.translate({ord('\n'): None})
	f.close()

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

	# File in data section
	f = open("solutions/data/p0011.txt", "r")
	numGrid = f.read()
	f.close()

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

	from functools import cache
	@cache
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

	from functools import cache
	@cache
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

def p0017() -> int:
	"""How many letters used writing out numbers 1 to 1000"""
	# 21124
	
	ones = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",
			8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12: "twelve",
			13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen",
			17:"seventeen", 18:"eighteen", 19:"nineteen"}
	tens = {20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty",
			70:"seventy", 80:"eighty", 90: "ninety"}

	def numToWord(remainder: int) -> str:
		ans = ""
		while remainder >= 1:
			if remainder >= 1000:
				x = remainder // 1000
				ans += ones[x] + "thousand"
				remainder -= (x * 1000)
			elif remainder >= 100:
				x = remainder // 100
				ans += ones[x] + "hundred"
				remainder -= (x * 100)
				if remainder > 0:
					ans += "and"
			elif remainder >= 20:
				x = remainder // 10
				ans += tens[x*10]
				remainder -= (x * 10)
			else:
				ans += ones[remainder]
				remainder -= remainder
		
		return ans
	
	return sum([len(numToWord(num)) for num in range(1, 1000+1)])

def p0018() -> int:
	"""Find the maximum total from top to bottom of the triangle in the data"""
	# 1074

	# File in data section
	f = open("solutions/data/p0018.txt", "r")
	fileStr = f.read()
	f.close()

	# Parse data
	lines = fileStr.split("\n")
	nums = [line.split(" ") for line in lines]

	triangle = {}
	for y, row in enumerate(nums):
		for x, col in enumerate(row):
			triangle[(y, x)] = int(col)
	
	# Compute answer
	from functools import cache
	@cache
	def largestSum(yCoord, xCoord):
		current = triangle[yCoord, xCoord]
		try:
			left = largestSum(yCoord + 1, xCoord)
			right = largestSum(yCoord + 1, xCoord + 1)
		except KeyError:
			return current

		return current + max(left, right)
	
	return largestSum(0, 0)

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
		
def p0023() -> int:
	"""Sum of all +ive ints which are not the sum of two abundant numbers"""
	# 4179871

	limit = 128123

	from helper import factors
	def abundant(n: int) -> bool:
		properFactors = factors(n)
		properFactors.remove(n)
		return sum(properFactors) > n

	# Using set to ensure faster `in` look ups
	abundants = set(n for n in range(limit) if abundant(n))

	notSumAbundants = []
	for n in range(limit+1):
		found = False
		for x in abundants:
			diff = n - x
			if diff in abundants:
				found = True
				break
			if diff < 0:
				break

		if found == False:
			notSumAbundants.append(n)

	return sum(notSumAbundants)

def p0024() -> int:
	"""What is the millionth lexicographic permutation of the digits 0 to 9?"""
	# 2783915460

	# itertools perumtations outputs in lexiographic order
	from itertools import permutations, islice
	iterable = permutations("0123456789")
	ansTuple = next(islice(iterable, 1_000_000, None))
	ans = int("".join(ansTuple))

	return ans

def p0025() -> int:
	"""Index of the first term in the Fibonacci sequence to have 1000 digits?"""
	# 4782

	fibs = [1,1]
	while len(str(fibs[-1])) < 1000:
		fibs.append(fibs[-1] + fibs[-2])

	return len(fibs)

def p0026() -> int:
	"""Find d < 1000 for which 1/d contains the longest recurring cycle"""
	# 983

	longestCycle, longestCycleD = 0, 0

	for d in range(2, 1_000):
		# Attempted optimisation that skips numbers with prime factors
		# 	of only 2 and 5 as these will be none recurring due to sharing
		# 	prime factors with the base (10). While it does work the time gain
		# 	is cancelled out with the time gain from calculating prime factors.
		remainder = 1
		partials = []
		while remainder > 0:
			remainder = (remainder  % d) * 10
			if remainder in partials: # Recurring number found
				cycleLength = len(partials) - partials.index(remainder)
				if cycleLength > longestCycle:
					longestCycle, longestCycleD = cycleLength, d
				break
			else:
				partials.append(remainder)

	return longestCycleD

def p0027() -> int:
	"""Find |a, b| < 1000 that n^2 + an + b results in longest set of primes."""
	# -59231

	from helper import isPrime
	from functools import cache
	isPrime = cache(isPrime)

	maxCount, ans = 0, 0 
	
	for a in range(-999, 1000):
		for b in range(1000): # b can't be negative as when n = 0 result = b
			n = 0
			count = 0
			while isPrime(candidate := n**2 + a * n + b):
				n += 1
				count += 1
			if count > maxCount:
				maxCount, ans = count, a * b

	return ans

def p0028() -> int:
	"""What is the sum of the diagonal numbers in a 1001^2 clockwise spiral?"""
	# 669171001

	num = 1
	count = 1
	for x in range(2, 1001, 2):
		for _ in range(4):
			num += x
			count += num

	return count

def p0029() -> int:
	"""No. Distinct terms are generated by a^b for 2 ≤ a & b ≤ 100?"""
	# 9183

	return len({a**b for a in range(2,100+1) for b in range(2,100+1)})

def p0036() -> int:
	"""Sum of all n < 1,000,000, which are palindromic in base 10 and 2."""
	# 872187

	acc = 0
	for n in range(1_000_000):
		if (base10 := str(n)) == base10[::-1] and \
			(base2 := format(n, "b")) == base2[::-1]:
			acc += n

	return acc

def p0067() -> int:
	"""Find the maximum total from top to bottom of the triangle in the data"""
	# 7273

	# File in data section
	f = open("solutions/data/p0067.txt", "r")
	fileStr = f.read()
	f.close()

	# Parse data
	lines = fileStr.split("\n")
	nums = [line.split(" ") for line in lines]

	triangle = {}
	for y, row in enumerate(nums):
		for x, col in enumerate(row):
			triangle[(y, x)] = int(col)
	
	# Compute answer
	from functools import cache
	@cache
	def largestSum(yCoord, xCoord):
		current = triangle[yCoord, xCoord]
		try:
			left = largestSum(yCoord + 1, xCoord)
			right = largestSum(yCoord + 1, xCoord + 1)
		except KeyError:
			return current

		return current + max(left, right)
	
	return largestSum(0, 0)
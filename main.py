# Imports
import importlib
import importlib.resources
# import unittest
import time

# Constants
multiProblem = False
singleProblem = 19
problemFrom = 1
problemTo = 100

# import solutions.p0001_0100Tests as tests
# unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(tests.p0001_0100Tests))
# # unittest.TextTestRunner().run(tests.p0001_0100Tests)


# Main program
globalStart = time.perf_counter()

# import solutions.p0001_0100 as solutions
solutions = importlib.import_module(f".p0001_0100", f"solutions")

solution = getattr(solutions, f"p{str(singleProblem).zfill(4)}")
print(f"Problem {str(singleProblem).zfill(4)} solution's is {solution()}")

# for i in range(problemFrom, problemTo+1):
# 	try:
# 		solution = getattr(solutions, f"p{str(i).zfill(4)}")
# 		print(f"Problem {str(i).zfill(4)} solution's is {solution()}")
# 	except AttributeError:
# 		print("Solutions found up to problem", i-1)
# 		break
			
print(time.perf_counter() - globalStart)
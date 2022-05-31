import unittest
import solutions.p0001_0100 as solutions

class t0001_0100(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		pass
        # import importlib.resources
        # cls.inputStrEx = importlib.resources.read_text(__package__, "inputEx.txt")
        # cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")
    
    # Example tests   
	def testp0001(self):
		self.assertEqual(solutions.p0001(), 233168)
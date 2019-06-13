#**Coin Flip Simulation** - Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of tails and heads.
import random

class CoinFlipper(object):
	def __init__(self, n):
		self.n = int(n)

	def solution(self):
		heads, tails = 0, 0
		for i in range(self.n):
			if random.randint(1,2) == 1:
				heads += 1
			else:
				tails += 1
		print("This time we had %i heads and %i tails" %(heads, tails))

if __name__ == "__main__":
	n = input("How many times are we flipping? \n> ")
	CoinFlipper(n).solution()
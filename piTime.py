#**Find PI to the Nth Digit** - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.

class PiCalculator(object):
	def __init__(self, n):
		self.n = int(n)+1

	def solution(self):

		print("feast your eyes on this pi(e)!\n" + eval('"{0:.'+str(self.n)+'f}".format(22/7)')[:-1]) if self.n < 53 else print("well so much for respecting the limit there, eh?")


if __name__ == "__main__":
	n = input("how many decimals of pi would you like? (limit is 52) \n> ")
	PiCalculator(n).solution()
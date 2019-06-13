#**Find e to the Nth Digit** - Just like the previous problem, but with e instead of PI. Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.

#note: Newton's series expansion of e is captured as the sum of (1/n!) as n approaches infinity. Let's have some fun with that.

def factorial(n): 
	result = 1
	for i in range(1,n):
		result *= i
	return result


class eCalculator(object):
	def __init__(self, n):
		self.n = int(n)+1
		

	def solution(self):	
		e = sum(1/factorial(n) for n in range(1,19)) # this is very ugly -- come back and clean it up
		# ran tests to find out lowest upper bound which maintains accuracy of 50 decimal places
		print("e!\n" + eval('"{0:.'+str(self.n)+'f}".format(e)')[:-1]) if self.n < 500 else print("well so much for respecting the limit there, eh?")



if __name__ == "__main__":
	n = input("how many decimals of e would you like? (limit is 50) \n> ")
	eCalculator(n).solution()
#**Fibonacci Sequence** - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

class Fibonacci(object):
	def __init__(self, n):
		self.n = int(n) 

	def solution(self):
		print("The Fibonacci number of %i is %i" %(self.n ,sum(range(self.n+1))))


if __name__ == "__main__":
	f = input("please enter a number! \n> ")
	Fibonacci(f).solution()
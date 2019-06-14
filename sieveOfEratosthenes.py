#**Sieve of Eratosthenes** - The sieve of Eratosthenes is one of the most efficient ways to find all of the smaller primes (below 10 million or so).

def sieveIt(remaining):
	for i in remaining[1:]:
		if i%remaining[0] == 0:
			remaining.remove(i)
	return(remaining)

class EratosthenesSieve(object):
	def __init__(self, n):
		self.n = int(n)

	def solution(self):
		primes = []
		possible = list(range(2,self.n+1))
		while len(possible) > 0:
			possible = sieveIt(possible)
			primes.append(possible.pop(0))
		print(primes)

if __name__ == "__main__":
	upper = input("Let's see a list of primes up to/including? \n> ")
	EratosthenesSieve(upper).solution()
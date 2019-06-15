#**Collatz Conjecture** - Start with a number *n > 1*. Find the number of steps it takes to reach 1, using the following process: If *n* is even, divide it by 2. If *n* is odd, multiply it by 3 and add 1.

n = int(input("Please enter a number and we will find its 'Collatz length'! \n> "))
steps = 0
while n != 1:
	if n % 2 == 0:
		n *= 1/2
		# print('Even! divide by 2: ', n) # for a curious user // debugging
	else:
		n = (3*n) + 1
		# print('Odd! multiply by three and add 1: ', n) # for a curious user // debugging
	steps += 1

print("It took %i steps to reach 1" %(steps))

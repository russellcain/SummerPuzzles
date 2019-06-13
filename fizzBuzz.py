#**Fizz Buzz** - Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

result = "1"
for i in range(2,100):
	text = ""
	if i % 3 == 0:
		text += "Fizz"
	if i % 5 == 0:
		text += "Buzz"
	if (i % 3 != 0 and i % 5 != 0):
		text = str(i)
	result += ", "+text
print(result + ", Buzz")
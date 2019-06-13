#**Reverse a String** - Enter a string and the program will reverse it and print it out.
class StringReverser(object):
	def __init__(self, givenString):
		self.givenString = givenString

	def solution(self):
		print("Reversed:", self.givenString[::-1] )

if __name__ == "__main__":
	givenString = input("What are we writing backwards? \n> ")
	StringReverser(givenString).solution()
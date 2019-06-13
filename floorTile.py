#**Find Cost of Tile to Cover W x H Floor** - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.

class TileCalculator(object):
	def __init__(self, length, width, cost):
		self.length = int(length)
		self.width = int(width) 
		self.cost = float(cost)

	def solution(self):
		print("Tiling this floor will cost you $" + str(self.length*self.width*self.cost))


if __name__ == "__main__":
	length = input("please enter the length of the room \n> ")
	width = input("and please enter the width of the room \n> ")
	cost = input("lastly, how much does one tile cost? \n> ")
	TileCalculator(length, width, cost).solution()
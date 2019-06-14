#**Closest pair problem** - The closest pair of points problem or closest pair problem is a problem of computational geometry: given *n* points in metric space, find a pair of points with the smallest distance between them.

"""Assumption: 
	* User will always be content with a Euclidean distance (squareroot of summed differences between squared pairs)
	* There is always one unique solution
"""

def distance(p1, p2):
	dif = 0
	for i in range(len(p1)):
		dif += (p1[i]**2 - p2[i]**2)
	return dif**(1/2)

class EratosthenesSieve(object):
	def __init__(self, points):
		self.points = points

	def solution(self):
		first = points
		second = points[1:]
		ourMin = [distance(first[0], second[0]), first[0], second[0]]
		for i in first[:-1]:
			for j in second:
				if distance(i,j) < ourMin[0]:
					ourMin = [min(ourMin, distance(i,j)), i, j]
			second.pop(0)
		print("The smallest distance is %i, between "%ourMin[0], ourMin[1], "and", ourMin[2])


if __name__ == "__main__":
	"""Need to find a good way to read in points and group into a list"""
	points = input("please enter the points in your metric space? \n> ")
	EratosthenesSieve(points).solution()
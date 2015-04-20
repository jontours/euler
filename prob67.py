f = open('p067_triangle.txt', 'r')
triangle = []
class Node:
	def __init__(self, left = None, right = None, value = None):
		self.left = left
		self.right = right
		self.value = value
	def out(self):
		print self.value
		if self.left:
			print self.left.value
		if self.right:
			print self.right.value
	
		

def build_graph():
	#print x
	graph = []
	for row in range(0, len(triangle) - 1):
		for column in range(0,row + 1):
			triangle[row][column].left = triangle[row + 1][column]
			triangle[row][column].right = triangle[row +1][column + 1]
			
			
		
		
		

for line in f:
	numbers = []
	for number in line.split():
		node = Node()
		node.value = int(number)
		numbers.append(node)
	triangle.append(numbers)

build_graph()
root = triangle[0][0]
root.out()


	
	


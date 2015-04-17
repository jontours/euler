#count = 0

map = {}
def traverse(x,y):
	global count
	
	#print x,y
	if map.get((x,y)):
		print x,y
		print map.get((x,y))
		return map.get((x,y))
	elif x == 0 and y == 0:
		#print count
		count += 1
		return count 
	elif x == 0:
		traverse(x, y - 1)
		return count
	elif y == 0:
		traverse(x -1, y )
		return count
	else:
		
		
		count += traverse(x - 1, y)
		count += traverse(x, y - 1)
		map[(x,y)] = count
		
		return count
		
count = 0
traverse(2,2)
print count

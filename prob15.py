#count = 0

map = {}
def traverse(x,y):
	
	
	print x,y
	if map.get((x,y)):
		print "in get"
		print x,y
		print map.get((x,y))
		
		return map.get((x,y))
	elif x == 0 and y == 0:
		#print count
		count = 1
		return count 
	elif x == 0:
		count = traverse(x, y - 1)
		map[(x,y)] = count
		
		return count
	elif y == 0:
		count = traverse(x -1, y )
		map[(x,y)] = count
		return count
	else:
		count = traverse(x - 1, y)
		count += traverse(x, y - 1)
		map[(x,y)] = count
		
		return count
		
print traverse(20,20)

print map

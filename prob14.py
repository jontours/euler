import operator

map = {}
map[1] = 1

def sequence(n):
    count = 0
    #print n
    if map.get(n):
        return map.get(n)
    elif n % 2 == 0:
        number = 1 + sequence(n/2)
        map[n] = number
        return number
    else:
        number = 1 + sequence(n * 3 + 1)
        map[n] = number
        return number

for n in range(500000, 1000000):
	sequence(n)

sorted_x = sorted(map.items(), key=operator.itemgetter(1), reverse=True)


for value in sorted_x:
    if value[1] <= 1000000:
        print value[0]
        print value[1]
        break


	
		
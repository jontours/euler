def isPrime(n):
    for m in range(2, int(n**0.5)+1):
        if not n%m:
            return False
    return True
def prime_factor(number):
	largestPrime = 1
	midway = int((number ** 0.5) + 1)
	
	for x in range (2, midway):
		if number == 1:
			break
		elif isPrime(x) and number % x == 0:
			if x > largestPrime:
				largestPrime = x
				number /= largestPrime
				
				
		"""		
		elif number % x == 0:
			if isPrime(number / x) and number / x > largestPrime  :
				largestPrime = number/ x
			else:
				continue
		"""
	return largestPrime

number = 600851475143
midway = (number ** 0.5) + 1
midway = int(midway)
#print midway
print prime_factor(number)


def is_palindrome(number):
	number = str(number)
	return number == number[::-1]
		
def find_first_palindrome(x,y):
	largest = 0
	for x in range(999, 100, -1):
		for y in range (999, 100, -1):
			if is_palindrome(x * y):
				candidate = x * y
				if candidate > largest:
					largest = candidate
	return largest

print find_first_palindrome(999,999)

			

	
#Largest palindrome product
import math

def largest_palindrome(max):
	i = max
	while i > 0:
		if check_if_palindrome(i) and check_product_of_two_three_digit_numbers(i):
			return i
		else:
			i -= 1
	return False

def check_if_palindrome(number):
	num_str = str(number)
	length = len(num_str)
	length_half = math.ceil(length / 2)
	i = 0
	while i < length_half:
		if num_str[i] != num_str[length - (1 + i)]:
			return False
		else:
			i += 1
	return True

def check_product_of_two_three_digit_numbers(number):
	i = 100
	while i < 1000:
		if (number % i == 0) and (len(str(number//i)) == 3):
			return True
		else:
			i += 1
	return False

print(largest_palindrome(999 * 999))
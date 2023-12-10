import math

#take square root and round up - this is the highest possible factor
#loop from 1 to this number

#check prime function
#loop from 1 to the number
#if there if division is mod 0
#600851475143

def return_largest_prime_factor(number):
	prime_factors = []
	max_factor = math.ceil(math.sqrt(number))
	for x in range(max_factor + 1):
		if x <= 1:
			continue
		if number % x == 0 and check_if_prime(x):
			prime_factors.append(x)
	return max(prime_factors)

def check_if_prime(number):
	max_factor = math.ceil(math.sqrt(number))
	for x in range(max_factor + 1):
		if x <= 1:
			continue
		elif number % x == 0:
			return False
		else:
			continue
	return True

print(return_largest_prime_factor(600851475143))

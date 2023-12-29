# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without 
# any remainder
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def is_prime(number):
	i = 2
	while i < number:
		if (number % i == 0): 
			return False
		else:
			i += 1
	return True

def all_primes_up_to_and_including_n(number):
	primes = [] 
	i = 2
	while i <= number:
		if is_prime(i):
			primes.append(i)
		i += 1
	return primes

def return_prime_factorization(number):
	prime_factors = []
	possible_prime_factors = all_primes_up_to_and_including_n(number)
	for prime in possible_prime_factors:
		remainder = number
		while remainder % prime == 0 and remainder > 1:
			remainder = remainder / prime
			prime_factors.append(prime)
	return prime_factors

def min_number_divisible_by_all_up_to_n(number):
	prime_factors = all_primes_up_to_and_including_n(number)
	i = 2
	prime_factors_with_multiple = {}
	while i <= number:
		prime_factors = return_prime_factorization(i)
		for prime in prime_factors:
			if prime in prime_factors_with_multiple:
				if prime_factors.count(prime) > prime_factors_with_multiple[prime]:
					prime_factors_with_multiple[prime] = prime_factors.count(prime)
			else:
				prime_factors_with_multiple[prime] = prime_factors.count(prime)
		i += 1
	print(prime_factors_with_multiple)
	result = 1
	for k in prime_factors_with_multiple:
		result = result * (k ** prime_factors_with_multiple[k])
		print(f'result is now {result} after multiplying by {k} to the {prime_factors_with_multiple[k]}')
	return result

#solution is 232792560

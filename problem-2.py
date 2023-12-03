import copy 

fibonacci = [1, 2]
sum = 0

while fibonacci[1] < 4000000:
	if fibonacci[1] % 2 == 0:
		sum += fibonacci[1]
	old_fibonacci = copy.copy(fibonacci)
	fibonacci[0] = old_fibonacci[1]
	fibonacci[1] = old_fibonacci[0] + old_fibonacci[1]

print(sum)
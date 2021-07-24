number = int(input('enter the number: '))
prime = True
if number < 2:
	prime = False
else:
	i = 2
	prime = True
	while i < number:
		if number % i == 0:
			prime = False
			break
		i = i + 1
print(prime)
# print("jayesh gurbani")
# print("0----")
# print(" ||||")
# print('*' * 10)
# price = 10
# print(price)
# name = input('what is your name? ')
# favorite_color = input('what is your favorite color')
# print(name + 'likes' + favorite_color)
# birth_year = input ('birth year: ')
# print(type(birth_year))
# age = 2021 - int(birth_year)
# print(type(age))
# course = '''
# hi chad,

# he is our first email to you.

# Thank you,
# The support team

# '''
# print(course)
# course = 'python for beginners'
# another = course[:]

# print(another)
# first = 'john'
# last = 'smith'
# message = first + ' [' + last + ' ] is a coder '
# print (message)
# course = ' python for beginners '
# print(course.upper())
# print(course.lower()) /
# course = 'Python for beginners'
# print('Python' in course )
# print (10 % 3)
# x = 10 
# x = x + 3 
# print (x)
# x = 10 
# x -= 3
# print (x)
# x = 10 + 3 * 2 
# print (x)
# x = (2 + 3) * 10 -3 
# print (x) 
# has_high_income = True 
# has_good_credit = True
# if has_high_income and has_good_credit:
#    print ("Eligible for loan")
# i = 1
# while i<=5:
# 	print (i)
# 	i = i + 1
# print ("done")
# changed

# temp = ''
# for item in 'python':
# 	temp = item + '.' + temp + '.' + item

# print(temp)
# secret_number = 9
# guess_count = 0
# guess_limit = 3 
# while guess_count < guess_limit :
# 	guess = int(input('guess: '))
# 	guess_count += 1
# 	if guess == secret_number :
# 		print ('you won!')
# 		break
# else: 
# 	print ('sorry you failed!')

# print(temp)
# for item in range(5, 10):
# 	print(item)
# for x in range(4):
# 	for y in range(3):
# 		print(f'({x}, {y})')
# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
# 	output = '' 
# 	for count in range(x_count):
# 		output += 'x'
# 		print(output)
numbers = [3, 6, 2, 10 ,8, 4]
max = numbers[0]
for number in numbers:
	if number > max:
		max = number
print(max)
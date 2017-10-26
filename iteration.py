# Make a local change
# Make another local change

# iteration pattern

# [1, 5, 7 ,8 , 4, 3]

def iterate(list):
	# standard for loop with range
	# for i in range(0, len(list)):
	# 	print list[i]

	# for each loop
	for item in list:
		print item

def print_scores(names, scores):
	for i in range(0, len(names)):
		print names[i] , " scored " , scores[i]


# filter pattern
def congratulations(names, scores):
	for i in range(0, len(names)):
		if (scores[i] == 100):
			print "Congrats", names[i], "! You got a perfect score!"

# accumulation pattern - a type of iteration
# keep track of other data as we go

def sum(numbers):
	total = 0
	for n in numbers:
		total += n

	return total


def max(numbers):
	current_max = numbers[0]
	for n in numbers:
		if n > current_max:
			current_max = n

	return current_max

def average_score(numbers):
	average = sum(numbers) / float(len(numbers))
	return average

def drop_lowest_two(numbers):
	lowest = numbers[0]
	for n in numbers:
		if n < lowest:
			lowest = n

	numbers.remove(lowest)

	new_lowest = numbers[0]
	for n in numbers:
		if n < new_lowest:
			new_lowest = n

	numbers.remove(new_lowest)

	return numbers

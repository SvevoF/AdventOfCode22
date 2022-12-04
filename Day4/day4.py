with open('./input.txt', 'r') as f:
	file = f.readlines()
	inputs = [line[:-1] for line in file]

sections = [line.split(',') for line in inputs]

def contained(sections):
	counter = 0
	for section in sections:
		# print(f"sections: {section}")
		if int(section[0].split('-')[0]) >= int(section[1].split('-')[0]) and int(section[0].split('-')[1]) <= int(section[1].split('-')[1]):
			counter += 1
		elif int(section[1].split('-')[0]) >= int(section[0].split('-')[0]) and int(section[1].split('-')[1]) <= int(section[0].split('-')[1]):
			counter += 1
		else:
			continue

	return counter

def overlap(sections):
	counter = 0
	for section in sections:
		first = True
		for i in range(int(section[0].split('-')[0]), int(section[0].split('-')[1]) + 1):
			#print(section)
			# print(i)
			if i in range(int(section[1].split('-')[0]), int(section[1].split('-')[1]) + 1) and first:
				counter += 1
				#print("here")
				#print(section)
				first = False

		else:
			continue

	return counter


print(f"Result for the first part: {contained(sections)}")
print(f"Result for the second part: {overlap(sections)}")


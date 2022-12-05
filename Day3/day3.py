with open('./input.txt', 'r') as file:
	inputs = file.readlines()

rucksacks = [line[:-1] for line in inputs]

# print(rucksacks)

def divide(rucksack):
	pocket1 = rucksack[:int(len(rucksack)/2)]
	pocket2 = rucksack[int(len(rucksack)/2):]
	return (pocket1, pocket2)

def value(character):
	if ord(character) > 96:
		value = ord(character) - 96
	if ord(character) < 91:
		value = ord(character) - 38
	return value

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

pockets = []

for rucksack in rucksacks:
	pockets.append(divide(rucksack))

# print(pockets)

repeated = []

for pocket in pockets:
	first = True
	for char in pocket[0]:
		if char in pocket[1] and first:
			# print(f"char: {char} with ASCII {ord(char)}")
			first = False
			repeated.append(value(char))

print(f"Solution of Part 1: {sum(repeated)}")

groups = []
badges = []

for rucksack in chunker(rucksacks, 3):
	groups.append(rucksack)

for group in groups:
	first = True
	for char in group[0]:
		if char in group[1] and char in group[2] and first:
			# print(char)
			first = False
			badges.append(value(char))

print(f"Solution of Part 2: {sum(badges)}")

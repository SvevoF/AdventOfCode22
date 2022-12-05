with open("./input.txt") as f:
	bags = f.readlines()

# print(bags)

total = 0
bags_tot = []

for line in bags:
	if line != "\n":
		total += int(line)
	else:
		bags_tot.append(total)
		total = 0

total = 0

for i in range(3):
	max_bag = max(bags_tot)
	print(f"{i+1} most carrying Elf carries {max_bag} calories")
	total += max_bag
	bags_tot.remove(max_bag)

print(f"Solution of Part 2: {total}")
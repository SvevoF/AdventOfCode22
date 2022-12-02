with open("./input.txt", 'r') as f:
	strategies = f.readlines()

values = {	'X':1, # A ROCK
			'Y':2, # B PAPER
			'Z':3  # C SCISSORS
}

results = { 'win':6,
			'loss':0,
			'draw':3
}

actual_results = { 	'X':0, # LOSS
					'Y':3, # DRAW
					'Z':6  # WIN
}

points = []

def result(opponent, player):

	point = 0
	point += values[player]
	# print(ord(opponent) - ord(player))
	if (ord(opponent) - ord(player)) == -23:
		# DRAW
		point += results['draw']
	elif (ord(opponent) - ord(player)) == -24 or (ord(opponent) - ord(player)) == -21:
		# WIN
		point += results['win']
	elif (ord(opponent) - ord(player)) == -22 or (ord(opponent) - ord(player)) == -25:
		# LOSS
		point += results['loss']
	else:
		print('no worki')
	points.append(point)
	print(point)

# print(ord('C') - ord('X'))

def result_new(opponent, result):
	point = 0
	point += actual_results[result]

	if result == 'Y':
		# DRAW
		point += values[chr(ord(opponent) + 23)]
	elif result == 'X':
		# LOSS
		point += values[chr(ord(opponent) + 22)] if chr(ord(opponent) + 22) in values else values[chr(ord(opponent) + 25)]
	elif result == 'Z':
		# WIN
		point += values[chr(ord(opponent) + 24)] if chr(ord(opponent) + 24) in values else values[chr(ord(opponent) + 21)]
	else:
		print('no worki')

	points.append(point)

for line in strategies:
	opponent, player = line.split(" ")
	# final += result(opponent, player)
	result_new(opponent, player[:-1])

result = sum(points)
print(result)

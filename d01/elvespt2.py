#d01 advent of code 


carryingNumber = 0
topThree = [0,0,0]
total = 0

f = open('txt.txt', "r")

for numbers in f:
	try:
		carryingNumber += int(numbers)
	except:
		topThree.append(carryingNumber)
		topThree = sorted(topThree)
		topThree = topThree[1:]
		carryingNumber = 0

total = sum(topThree)
print(topThree, ',')
print(total)


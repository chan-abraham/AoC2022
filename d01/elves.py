#d01 advent of code 


maxNumber = 0
carryingNumber = 0


f = open('txt.txt', "r")

for numbers in f:
	try:
		carryingNumber += int(numbers)
	except:
		if maxNumber < carryingNumber:
			maxNumber = carryingNumber
		carryingNumber = 0

print(maxNumber)


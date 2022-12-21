#adventofcoded04


f = open ('txt.txt')

i = 0
x = []
y = []


for line in f:
	backpack = line.strip()
	x = backpack.split(",")
	y = x[0].split("-") + x[1].split("-")
	if int(y[0]) >= int(y[2]) and int(y[1]) <= int(y[3]):
		i += 1
		print(y, i)
	if int(y[0]) <= int(y[2]) and int(y[1]) >= int(y[3]):
		i += 1
		print(y, i)
	if int(y[0]) == int(y[2]) and int(y[1]) == int(y[3]):
		i -= 1
		print ("repeated")

		

	


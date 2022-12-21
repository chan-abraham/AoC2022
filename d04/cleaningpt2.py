#adventofcoded04


f = open ('txt.txt')

counter = 0
x = []
y = []


def ft_overlap(y):
	#if these numbers are between those numbers, there will be overlap
	if int(y[2]) <= int(y[0]) <= int(y[3]):
		return (1)
	if int(y[2]) <= int(y[1]) <= int(y[3]):
		return (1)
	if int(y[0]) <= int(y[2]) <= int(y[1]):
		return (1)
	if int(y[0]) <= int(y[3]) <= int(y[1]):
		return (1)

	return (0)


for line in f:
	backpack = line.strip()
	x = backpack.split(",")
	y = x[0].split("-") + x[1].split("-") #parsing
	if ft_overlap(y): #returns 1 if overlap
		counter += 1
		print(y, counter)
	else:
		print(y, counter, "no overlap")


		

	


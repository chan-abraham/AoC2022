#adventofcoded03



i = 0
j = 0
k = 0
priority = 0
length = 0
onoff = 0
linecounter = 0
compartment = ['x' ,'y' ,'z' ] 

f = open ('txt.txt')


def get_priority(sameNumber):
#	print('the value is', sameNumber, ord(sameNumber))
	if 65 <=ord(sameNumber) <= 90:
	#	print(ord(sameNumber)-38, 'upper case')
		return (ord(sameNumber)-38)
#	print(ord(sameNumber)-96, 'lower case')
	return(ord(sameNumber)-96)
	print("error")
	return(0)

for line in f:
	backpack = line.strip()
	length = len(backpack)
	#print(compartment)
	compartment[linecounter] = backpack
	#print(linecounter)
	if linecounter == 2:
		linecounter = -1
		while i <= len(compartment[0]) -1:
			while j <= len(compartment[1]) -1:
				if compartment[0][i] == compartment[1][j]:
					while k <= len(compartment[2]) - 1:
						if compartment[0][i] == compartment[1][j] == compartment[2][k]:	
							#print('priority is', priority)
							#print('letters are', compartment[0][i], compartment[1][j], compartment[2][k])
							onoff = 1
							priority = priority + get_priority(compartment[0][i])
							break
						k+=1
				j += 1
				if k == length or onoff == 1:
					k = 0
					break
			i += 1
			j = 0
			if onoff == 1:
				onoff = 0
				break
	linecounter += 1
	i = 0
	j = 0
print(priority)

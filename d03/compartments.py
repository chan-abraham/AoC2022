#adventofcoded03



i = 0
j = 0
priority = 0
length = 0
test = 1
onoff = 0

f = open ('txt.txt')


def get_priority(sameNumber):
	print('the value is', sameNumber, ord(sameNumber))
	if 65 <=ord(sameNumber) <= 90:
		print(ord(sameNumber)-38, 'upper case')
		return (ord(sameNumber)-38)
	print(ord(sameNumber)-96, 'lower case')
	return(ord(sameNumber)-96)
	print("error")
	return(0)

for line in f:
	backpack = line.strip()
	length = len(backpack)//2
	compartment1 = backpack[:length]
	compartment2 = backpack[length:]
	print("test", test)
	while i <= length - 1:
		while j <= length -1:
			if compartment1[i] == compartment2[j]:	
				#print(priority)
				#print(compartment1[i])
				#print(get_priority(compartment1[i]))
				onoff = 1
				priority = priority + get_priority(compartment1[i])
				break
			j += 1
		i += 1
		j = 0
		if onoff == 1:
			onoff = 0
			break
	test += 1
	i = 0
	j = 0
print(priority)

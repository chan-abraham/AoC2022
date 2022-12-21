#d02 of Advent of Code


currentLetter = "a"
winner = 0
rps = 0
score = 0


def winorlose(currentLetter):
	if currentLetter[0] == "A":
		if currentLetter[2] == "X":
			return(3)
		elif currentLetter[2] == "Y":
			return(6)
		elif currentLetter[2] == "Z":
			return(0)
	elif currentLetter[0] == "B":
		if currentLetter[2] == "X":
			return(0)
		elif currentLetter[2] == "Y":
			return(3)
		elif currentLetter[2] == "Z":
			return(6)
	elif currentLetter[0] == "C":
		if currentLetter[2] == "X":
			return(6)
		elif currentLetter[2] == "Y":
			return(0)
		elif currentLetter[2] == "Z":
			return(3)
	return(0)

def scoreFT(currentLetter):
	if currentLetter[2] == "X":
		return(1)
	elif currentLetter[2] == "Y":
		return(2)
	elif currentLetter[2] == "Z":
		return(3)
	return (0)

with open('txt.txt') as f:
	while True: 
		currentLetter = f.read(4)
		if not currentLetter:	
			print("done")
			break
		winner = winorlose(currentLetter)
		print(winner)
		rps = scoreFT(currentLetter)
		print(rps)
		score = score + rps + winner
		
print(score)



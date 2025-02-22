#Create list of teams:

from random import randrange

def get_averages():
	teamsList = []

	while len(teamsList) <= 15:
		team = randrange(1, 17)
		if teamsList.count(team) == 0:
			teamsList.append(team)
			team = randrange(1, 17)
		else:
			team = randrange(1, 17)

#Compare Pairs from list:
#pairs can be the same each time, because the value of the pair is random
#only want a determined winner if the teams are 5 or more ranks apart, otherwise it can be "random"
#else covers if team 1 is significantly better or if it is close

	courtC = 0
	courtB = 0
	i = 0

	while i <= 14:
		if teamsList[i] - teamsList[i+1] >= 8:
			courtC = courtC + teamsList[i]
			courtB = courtB + teamsList[i + 1]
			i = i + 2
		else:
			courtC = courtC + teamsList[i+1]
			courtB = courtB + teamsList[i]
			i = i + 2

	averageC = courtC / 8
	averageB = courtB / 8

#	print("Court B is: " + str(averageB))
#	print("Court C is: " + str(averageC))
	return(str(averageB), str(averageC))



C = 0
B = 0
count = 1

#run through the average a set number of times, this case:1000

while count <= 1000:
	averageB, averageC = get_averages()
	B = B + float(averageB)
	C = C + float(averageC)
	count = count + 1

resultB = B / 1000
resultC = C / 1000

print("The average rank of court B over 1000 iterations is: " + str(resultB))
print("The average rank of court C over 1000 iterations is: " + str(resultC))

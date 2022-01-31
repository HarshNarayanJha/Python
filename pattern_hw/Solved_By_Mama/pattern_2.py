# 2 (By Mama)
"""
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
"""

totalLevels = 5
currentLevel = 1
firstDigit = 1
prevlevelNums = []
currentlevelNums = []
offset = 0

while True:
	if currentLevel > totalLevels:
		break
	toPrint = ""
	toPrint += " "*(totalLevels - currentLevel)
	currentlevelNums = []
	for i in range(0, currentLevel):
		NumToPrint = 0
		if i == 0:
			NumToPrint = firstDigit
		else:
			for idx in range(i-1, i+1):
				if idx < len(prevlevelNums):
					NumToPrint += prevlevelNums[idx]
		currentlevelNums.insert(i, NumToPrint)
		toPrint += " " + str(NumToPrint)
	
	print(toPrint)
	currentLevel = currentLevel + 1
	prevlevelNums = currentlevelNums.copy()


    
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

#Source Geeks for Geeks
#Method 1: Using nCr formula i.e. n!/(n-r)!r!
#After using nCr formula, the pictorial representation becomes:
#         0C0
#      1C0   1C1
#   2C0   2C1   2C2
#3C0   3C1   3C2    3C3
from math import factorial
levels = 8
for i in range(levels):
    print(" "*(levels-(i+1)),end="")
    for j in range(i+1):
        print(factorial(i)//(factorial(i-j)*factorial(j)),end=" ")
    print()

	prevlevelNums = currentlevelNums.copy()


    

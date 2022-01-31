# 18 (By Mama)
"""
      *
     ***
    *****
   *******
  *********
   *******
    *****
     ***
      *
"""

totalLevels = 9 # change this to 9 for assignment
# currentLevel = 1
startSpace = totalLevels

for i in range(totalLevels):
  if i <= totalLevels / 2:
    startSpace -= 1
    toPrint =  " " * startSpace + "*" * (1 + (2 * i))
    # toPrint = str(i) + " " +str((1+(2*i)))
  else:
    startSpace += 1
    toPrint =  " "*startSpace + "*" * ((2 * (totalLevels - i)) - 1)
    # toPrint = str(i) + " - " + str((2*(totalLevels- i))-1)
  print(toPrint)
# 18
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

for i in range(6, -6, -1):
    print(' ' * (abs(i)), end='')
    for j in range(7-i):
        print("*", end='')
    print()
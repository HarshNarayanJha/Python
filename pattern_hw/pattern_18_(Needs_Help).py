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

for i in range(4, -5, -1):
    print(' ' * (abs(i)), end='')
    print("*"*(2*(5-abs(i))-1), end='')
    print()

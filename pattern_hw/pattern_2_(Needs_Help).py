# 2
"""
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
"""

spaces = [4, 3, 2, 1, 0]

for i in spaces:
    print(" "*i, end='')
    print("1 "*(5-i))
    
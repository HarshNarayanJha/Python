# 3
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

num_levels = 9
spaces = list(range(num_levels//2, 0, -1)) + list(range(0, num_levels//2 + 1))

for i in spaces:
    print(" " * i, end='')
    print("*" * (spaces[0] + 1 - i), end="*" * (spaces[0] - i)+"\n")
    
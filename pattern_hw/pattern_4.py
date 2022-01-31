# 4
"""
   1
  212
 32123
4321234
 32123
  212
   1
"""

max_num = 4
spaces = list(range(max_num - 1, 0, -1)) + list(range(0, max_num))

for i in spaces:
    print(" " * i, end='')

    for j in sorted(list(range(spaces[0] + 1 - i)), reverse=True):
        print(j + 1, end='')

    for k in list(range(spaces[0] - i)):
        print(k + 2, end='')
        
    print()
    
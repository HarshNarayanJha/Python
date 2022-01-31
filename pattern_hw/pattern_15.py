# 15
"""
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
"""

upto = 5

spaces = list(range(upto - 1, 0, -1)) + list(range(0, upto))

for i in spaces:
    print(' ' * i, end='')

    for j in range(upto - i):
        print(j + 1, end=' ')

    print()
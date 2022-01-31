# 24
# Made In one go!
"""
1 2 3 4 5
 2 3 4 5
  3 4 5
   4 5
    5
   4 5
  3 4 5
 2 3 4 5
1 2 3 4 5
"""

upto = 5

for i in list(range(upto)) + list(range(upto - 2, -1, -1)):
    print(' ' * i, end='')

    for j in range(i, upto):
        print(j + 1, end=' ')
    print()
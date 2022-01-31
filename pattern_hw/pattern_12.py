# 12
"""
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
"""

num_levels = 5

for i in range(num_levels):
    print(" " * (num_levels - 1 - i), end='')
    for j in range(i + 1):
        print(j + 1, end=' ')
    print()
# 19
"""
      *
     **
    ***
   ****
  *****
 ******
*******
"""

num_levels = 7

for i in range(num_levels):
    print(' ' * (num_levels - 1 - i), end='*' * (i + 1))
    print()
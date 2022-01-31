# 17
"""
      *
     ***
    *****
   *******
  *********
 ***********
"""

num_levels = 6

for i in range(num_levels):
    print(' ' * (num_levels - i), end="*" * (i * 2 + 1))
    print()
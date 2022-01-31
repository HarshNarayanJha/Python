# 21
"""
*******
*    *
*    *
*    *
*    *
*******
"""

num_levels = 6

for i in range(num_levels):
    if i == 0 or i == num_levels - 1:
        print('*' * 7)
    else:
        print('*' + ' ' * 4 + '*')
# 25
"""
A
BC
DEF
GHIJ
KLMNO
"""

num_levels = 5

for i in range(num_levels * 3):
    print(chr(65 + i), end='')

    if i in [0, 2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77]:
        print()
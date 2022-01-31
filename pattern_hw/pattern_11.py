# 11
# (On first Try!)
"""
A
BB
CCC
DDDD
EEEEE
"""

num_levels = 5

for i in range(num_levels):
    for j in range(i + 1):
        print(chr(65 + i), end='')
    print()
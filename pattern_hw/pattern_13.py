# 13
"""
5
54
543
5432
54321
"""

num_levels = 5

for i in range(num_levels, 0, -1):
    for j in range(num_levels, i - 1, -1):
        print(j, end='')
    print()
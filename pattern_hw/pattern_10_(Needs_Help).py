# 10
"""
1
01
101
0101
10101
"""

num_levels = 5

for i in range(1, num_levels + 1):
    for j in range(i):
        for k in sorted([0, 1], reverse = (i % 2 != 0)):
            print(k, end='')
            # print(i, j, k, end=' _ ')
    print()
# 23
"""
12345
2345
345
45
5
45
345
2345
12345
"""

upto = 5

for i in list(range(upto)) + list(range(upto - 2, -1, -1)):
    for j in range(i, upto):
        print(j + 1, end='')
    print()
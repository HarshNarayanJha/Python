# 8
"""
1
12
123
1234
12345
1234
123
12
1
"""

upto = 5
lengths = list(range(1, upto)) + list(range(upto, 0, -1))

for i in lengths:
    for j in range(i):
        print(j + 1, end='')
    print()
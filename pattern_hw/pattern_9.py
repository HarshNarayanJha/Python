# 9
"""
12345
1234
123
12
1

1
12
123
1234
12345
"""

upto = 5
lengths = list(range(upto, 0, -1)) + list(range(0, upto + 1))

for i in lengths:
    for j in range(i):
        print(j + 1, end='')
    print()
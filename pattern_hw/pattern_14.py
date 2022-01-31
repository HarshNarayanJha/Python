# 14
"""
1****
12***
123**
1234*
12345
"""

num_levels = 5

for i in range(num_levels):
    for j in range(i + 1):
        print(j + 1, end='')
    print('*' * (num_levels - 1 - i), end='')
    print()
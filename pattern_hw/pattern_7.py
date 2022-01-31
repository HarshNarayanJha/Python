# 7
"""
1
22
333
4444
55555
"""

upto = 5

for i in range(upto):
    for j in range(i + 1):
        print(str(i + 1) * (i + 1), end='')
        break
    print()
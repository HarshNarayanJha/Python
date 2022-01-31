# 6
"""
Enter a number between 1 to 9 : 4
   1   
  121
 12321
1234321 
"""

height = int(input("Enter a number between 1 to 9 : "))
if height > 9 or height < 1: raise SystemExit(f"{height} is not between 1 and 9.")

for i in range(height):
    print(' '*(height - i - 1), end='')
    for j in range(i + 1):
        print(j + 1, end='')
    for k in range(i):
        print(k + 1, end='')
    print()
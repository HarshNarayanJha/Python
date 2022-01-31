# 5
"""
      A
     B B 
    C   C
   D     D
  E       E
 F         F
G           G
 F         F
  E       E
   D     D
    C   C
     B B
      A

"""

spaces = [6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6]
letter_counter = 0
incrementer = 1

for i in spaces:
    print(' '*i, end=f"{chr(65+letter_counter)}" + ' '*(6-i)*2 + f"{chr(65+letter_counter)}" + "\n")

    if i == 0:
        incrementer = -1

    letter_counter += incrementer
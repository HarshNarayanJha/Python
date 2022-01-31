# 1
""" 
1  
2 3  
4 5 6  
7 8 9 10  
11 12 13 14 15  
"""

# for i in range(15):
#     for j in range(i, 15):
#         print(j, end=' ')
#         # print(i, counter)
#         counter += i

upto = 15
counter = 0
# next_bresak = 1
breaks = [1, 3, 6, 10]
# incrementer = 2

while counter < upto:

    print(counter + 1, end=' ')

    # if counter + 1 == next_break:
    #     print()
    #     next_break += incrementer

    if counter + 1 in breaks:
        print()

    # print(counter, next_break, end='     ')
    counter += 1
    # incrementer += 1
# 22
"""
*       *****************       *
**      ********  *******      **
***     *******    ******     ***
****    ******      *****    ****
*****   *****        ****   *****
******  ****          ***  ******
******* ***            ** *******
**********              *********
"""

w_scale_factor = 8
for i in range(w_scale_factor):
    print('*' * (i + 1) + ' ' * (w_scale_factor - 1 - i) + '*' * (w_scale_factor + 1 - i) + ' ' * i * 2 + '*' * (w_scale_factor + 1 - i) + ' ' * (w_scale_factor - 1 -i) + '*' * (i + 1))
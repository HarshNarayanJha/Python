# Find the largest/smallest number in a list/tuple

nums_list = [2, 3, 1, 33, 6, 1, 88, 4, 5, 6, 97, 45, 13, 26, -6, -4, -8, 2, -45]
nums_tuple = (2, 3, 1, 45, 45, 13, 26, -6, -4, -8, 2, -45)

# Lists
largest = nums_list[0]
for i in nums_list:
    if i > largest:
        largest = i

smallest = nums_list[0]
for i in nums_list:
    if i < smallest:
        smallest = i

print(nums_list)
print(f"Largest: {largest}, Smallest: {smallest}\n")

# Tuples
largest = nums_tuple[0]
for i in nums_tuple:
    if i > largest:
        largest = i

smallest = nums_tuple[0]
for i in nums_tuple:
    if i < smallest:
        smallest = i

print(nums_tuple)
print(f"Largest: {largest}, Smallest: {smallest}")
### Linear seach and counting the frequency of elements
import random

# `ls` would just be a shuffled list of random numbers from 1 to 20.
# The amount of numbers is also random between 5 and 10
ls = random.sample(range(1, 20), random.randint(5, 10))
random.shuffle(ls)
print(f"The List: {ls}")

print()

## Linear search
num_to_find = random.choice(range(1, 20))     # Just take a random number in range(1, 20) to search for...
num_in_list = False
num_index = -1
for i in range(len(ls)):
    if ls[i] == num_to_find:
        num_in_list = True
        num_index = i

if num_in_list:
    print(f"{num_to_find} was found in list at index {num_index} !!!")
else:
    print(f"{num_to_find} was not found in list.")

print(f"Again, there are simple methods to do things,\nindex = ls.index(num_to_find) if num_to_find in ls else None")
simple_index = ls.index(num_to_find) if num_to_find in ls else None
print(f"index = {simple_index}" if simple_index is not None else f"index = {simple_index}, Not found")

print("\n")
## frequency of elements
# We have to create new list, as ls contains each element only one time
# Now numbers are sure repeated
ls = random.sample(list(range(1, 10))*100, random.randint(10, 20))
ls.sort()
print(f"New List: {ls}")

unq_nums = []
for i in ls:
    if i not in unq_nums:
        unq_nums.append(i)

# print(unq_nums)

freq_list = []
count = 0
prev = ls[0]
for i in ls:
    if i == prev:
        count += 1
    else:
        freq_list.append(count)
        count = 1
        prev = i
        continue

freq_list.append(count)

# print(freq_list)
frequencies = []
for i in range(len(unq_nums)):
    frequencies.append( [unq_nums[i], freq_list[i]] )

print("# Frequencies #")
for i in frequencies:
    print(f"{i[0]}: {i[1]}")

print("\nSimple way,\nfrom collections import Counter\nCounter(ls)")
from collections import Counter
simple_frequncies = Counter(ls)
for i, j in zip(simple_frequncies.keys(), simple_frequncies.values()):
    print(f"{i}: {j}")

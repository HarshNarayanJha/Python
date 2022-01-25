### To find the maximum, the minim value and the mean of the values in a list of numbers
import random

# `ls` would just be a shuffled list of random numbers from 1 to 20.
# The amount of numbers is also random between 5 and 10
ls = random.sample(range(1, 20), random.randint(5, 10))
random.shuffle(ls)
print(f"The List: {ls}")

print()
## Minimum
min_val = ls[0]
for i in ls:
    if i < min_val:
        min_val = i

print(f"Minimum = {min_val}")
print(f"Or simply, Minimim = min(ls) = {min(ls)}")

print()
## Maximum
max_val = ls[0]
for i in ls:
    if i > max_val:
        max_val = i

print(f"Maximum = {max_val}")
print(f"Again simply, Maximim = max(ls) = {max(ls)}")

print()
## Mean

# Find the sum
# val_sum = 0
# for i in ls:
#     val_sum += i

# Or, the smart method: use sum(ls)

mean = sum(ls) / len(ls)    # Mean = sum_of_elemnents / no_of_elements
print(f"Mean = {mean}")
# Or, again simply
import statistics
print(f"Again Simply, Mean = statistics.mean(ls) = {statistics.mean(ls)}")
del statistics
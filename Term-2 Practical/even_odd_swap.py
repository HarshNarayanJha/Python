# Input a list of numbers and swap elements at the even location with the elements at the odd location

nums = []
nums.append(int(input("Input first Number: ")))

get_num = True
while get_num:
    in_num = input("Input next number (hit enter/return without typing to stop): ")
    if not in_num:
        get_num = False
        break

    nums.append(int(in_num))

print(nums)
print("Swapping...\n")

for i in range(len(nums)):
    if i % 2 != 0:
        nums[i], nums[i-1] = nums[i-1], nums[i]

print(nums)

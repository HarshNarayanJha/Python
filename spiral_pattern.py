
def pad(n, d):
	z = "0"* (d - len(str(n)))
	return f"{z}{n}"

l = int(input("Enter length> "))
a = int(input("Enter height> "))
print()

nums = list(range(1, (l*a)+1))
nums = [pad(x, len(str(nums[-1]))) for x in nums]
row = 0
col = 0

arr = []

for x in range(a):
	arr.append([])
	for y in range(l):
		arr[x].append(0)
		
def move_left(x, y): return x, y-1
def move_right(x, y): return x, y+1
def move_up(x, y): return x-1, y
def move_down(x, y): return x+1, y

func_next = {move_right: move_down,
			 move_down: move_left,
			 move_left: move_up,
			 move_up: move_right}
last_dir = None
next_dir = None

while True:
	#print(row, col)
	
	if arr[row][col] == 0:
		arr[row][col] = nums.pop(0)
		
	if (row, col) == (0, 0):
		row, col = move_right(row, col)
		
		last_dir = move_right
		next_dir = func_next[last_dir]
			
	elif (row, col) == (0, l-1) and arr[row+1][col] == 0:
		row, col = move_down(row, col)
		
		last_dir = move_down
		next_dir = func_next[last_dir]
		
	elif (row, col) == (a-1, l-1) and arr[row][col-1] == 0:
		row, col = move_left(row, col)
		
		last_dir = move_left
		next_dir = func_next[last_dir]
		
	elif (row, col) == (a-1, 0):
		row, col = move_up(row, col)
		
		last_dir = move_up
		next_dir = func_next[last_dir]
		
	else:
		#print(last_dir, next_dir)
		if arr[last_dir(row, col)[0]][last_dir(row, col)[1]] == 0:
			row, col = last_dir(row, col)
			
		elif arr[next_dir(row, col)[0]][next_dir(row, col)[1]] == 0:
			row, col = next_dir(row, col)
			last_dir = next_dir
			next_dir = func_next[last_dir]
			
		else: break
			

for i in arr:
	print(*i)
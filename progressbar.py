import time
import random

TOTAL = 20

for i in range(TOTAL):
    bars = "■" * (i+random.randint(1,4))
    spaces = "□" * (TOTAL - len(bars))
    
    time.sleep(random.randint(0,3))
    print(f"|{bars}{spaces}|", end='\r')

print()
print("Done playing?!")
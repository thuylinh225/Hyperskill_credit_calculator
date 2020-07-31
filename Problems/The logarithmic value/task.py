import math
num = int(input())
base = int(input())
if base > 1:
    print(round(math.log(num, base), 2))
else:
    print(round(math.log(num), 2))

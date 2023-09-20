import math
import random as rd

tal = 10000000
cnt = 0
for i in range(0, tal + 1):
    x = rd.uniform(2, 3)
    y = rd.uniform(0, 13)
    if y <= x * x + 4 * x * math.sin(x):
        cnt += 1

print(cnt / tal * 13)

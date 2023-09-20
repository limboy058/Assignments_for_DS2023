import random as rd
from math import sqrt
#蒙特卡洛方法
cnt=0
tal=1000000
for i in range(0,tal):
    x=rd.uniform(0,1)
    y=rd.uniform(0,1)
    if x*x+y*y <= 1:
        cnt+=1
print("迭代%10d次 为%.10f"%(tal,cnt*4/tal))

#割圆法
d=sqrt(2) #边长
n=4 #边数
r=1 #半径
tal=20 #循环次数
for i in range(0,tal):
    d=sqrt(d*d/4+pow(r-sqrt(r*r-d*d/4),2))
    n=2*n
print("迭代%10d次 为%.10f"%(tal,n*d/2/r))

#
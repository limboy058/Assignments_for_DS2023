print('输入需要为整数:')
n=int(input())
l=-abs(n)
r=abs(n)

while r-l>1e-12:
    mid=(l+r)/2
    if pow(mid,3)<n:
        l=mid
    elif pow(mid,3)>n:
        r=mid
    else:
        l=r=mid
        
print(l)
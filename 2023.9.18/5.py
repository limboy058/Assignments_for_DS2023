def nd_sqrt(n):
    if n<=1:
        ret=1
    else:
        ret=n
    while(abs(ret*ret-n)>0.000000001):
        ret-=(ret*ret-2)/(2*ret)
    return ret

print(nd_sqrt(2))
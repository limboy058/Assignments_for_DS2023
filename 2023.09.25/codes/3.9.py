import random as rd


def solve(n: int):
    A = []
    for i in range(0, n):
        A.append(rd.randint(1, 5))
    print(A)
    B = [0 for x in range(0, n)]
    pre = [1 for x in range(0, n)]  # pre[i]=A[0]*A[1]*...*A[i-1]
    suf = [1 for x in range(0, n)]  # suf[i]=A[i+1]*A[i+2]*...*A[n-1]
    for i in range(1, n):
        pre[i] = pre[i - 1] * A[i - 1]
    for i in range(n - 2, -1, -1):
        suf[i] = suf[i + 1] * A[i + 1]
    for i in range(0, n):
        B[i] = pre[i] * suf[i]
    print(B)


solve(10)

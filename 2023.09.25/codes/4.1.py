def ksm(a: int, b: int, m: int):
    ans = 1
    while b != 0:
        if b & 1:
            ans = ans * a % m
        b >>= 1
        a = a * a % m
    return ans


def MR(x: int):
    if x < 3:
        return x == 2
    if x % 2 == 0:
        return False
    A = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    d = x - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in A:
        v = ksm(a, d, x)
        if v <= 1 or v == x - 1:
            continue
        for i in range(0, r):
            v = v * v % x
            if v == x - 1 and i != r - 1:
                v = 1
                break
            if v == 1:
                return False
        if v != 1:
            return False
    return True


print(9, MR(9))
print(17, MR(17))
print(169, MR(169))
print(1000000007, MR(100000007))
print(9355692578367837, MR(9355692578367837))
print(100000000000001921, MR(100000000000001921))

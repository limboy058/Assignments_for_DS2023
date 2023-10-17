def nd_cbrt(n):
    ret = 1
    if (n < 0):
        ret = -1
    i = 0
    while (abs(ret**3 - n) > 1e-12):
        ret -= (ret**3 - n) / (3 * ret * ret)
        i += 1
    print("迭代了", i, "次")
    return ret


print(nd_cbrt(10))
print(nd_cbrt(11345))
print(nd_cbrt(0.79))
print(nd_cbrt(-2))
print(nd_cbrt(0))

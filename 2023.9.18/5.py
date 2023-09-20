def nd_sqrt(n):
    if n < 0:
        print("error")
        return -1
    ret = n
    i = 0
    while (abs(ret * ret - n) > 1e-12):
        ret -= (ret * ret - n) / (2 * ret)
        i += 1
    print("迭代了", i, "次")
    return ret


print(nd_sqrt(1345))
print(nd_sqrt(0.79))
print(nd_sqrt(-2))

def my_sqrt(n, d):
    if n < 0 or d <= 0:
        return "输入有误"
    else:
        tmp = 0
        i = 0
        while abs(tmp * tmp - n) > d:
            if tmp * tmp > n:
                break
            tmp += d
            i += 1
        print("迭代了", i, "次")
        return tmp


print(my_sqrt(2, 0.00001))
print(my_sqrt(1001, 0.000001))

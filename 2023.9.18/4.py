def my_sqrt(n, d):
    if n < 0 or d <= 0:
        return "输入有误"
    else:
        tmp = 0
        while abs(tmp * tmp - n) > d:
            if tmp * tmp > n:
                break
            tmp += d
        return tmp


print(my_sqrt(2, 0.00001))
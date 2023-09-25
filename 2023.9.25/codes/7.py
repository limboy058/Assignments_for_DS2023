def my_gcd(a, b):
    while b != 0:
        tmp = a
        a = b
        b = tmp % b
    return a


print(my_gcd(15, 0))
print(my_gcd(15, 20))

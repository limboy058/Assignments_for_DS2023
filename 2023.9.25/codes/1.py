def d_to_b(f):
    judge = False
    if f[0] == '-':
        f = f.replace('-', '')
        judge = True
    tmp = f.split('.')
    l_d = -1
    r_d = -1
    l_d = int(tmp[0])
    if len(tmp) == 2:
        r_d = float("0." + tmp[1])

    l_b = ""
    r_b = ""
    while l_d != 0:
        l_b = chr(l_d % 2 + 48) + l_b
        l_d //= 2
    k = 0.5
    while r_d > 1e-30:
        if r_d >= k:
            r_b += '1'
            r_d -= k
        else:
            r_b += '0'
        k /= 2

    if l_b == "":
        l_b = "0"
    if r_b == "":
        if judge: return "-" + l_b
        return l_b
    if judge: return "-" + l_b + '.' + r_b
    return l_b + '.' + r_b


print(d_to_b(input()))

print(d_to_b(input()))

print(d_to_b(input()))

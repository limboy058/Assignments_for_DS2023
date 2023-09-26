import re


def chk(s):
    if re.match(r"^[1-9]\d{5}(18|19|20)\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}([0-9]|X)$",s):
        return True
    else:
        return False


print(chk(input()))

print(chk(input()))

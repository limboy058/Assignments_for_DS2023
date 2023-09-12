judge=False
s=input()
c=s[0]
for i in range(1,len(s)):
    if s[i]==c:
        judge=True;
        break;
    else:
        c=s[i]
print(judge)
print('请用空格分开输入的数字')
s=input()
v=[]
for item in s.split(' '):
    v.append(int(item))
v.sort();
for item in v:
    print(item,end=' ')
print()
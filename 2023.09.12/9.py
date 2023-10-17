print('请输入形如:')
print('[1,2,3,4,5]')
print('的一行')

s=input()
s=s[1:len(s)-1:1]

v=[]
for item in s.split(','):
   v.insert(0,int(item)) 
print(v)


v1=s.split(',')
v2=[]
idx=len(v1)-1
while idx>=0:
   v2.append(int(v1[idx]))
   idx=idx-1
print(v2)
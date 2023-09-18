n=int(input())
if n==1:
    print(1);
elif n==2:
    print(2);
else:
    if n%3==0:
        for i in range(0,n//3):
            print(3,end=" ")
        print()
    elif n%3==1:
        for i in range(0,(n-4)//3):
            print(3,end=" ")
        print(2,2)
    else:
        for i in range(0,(n-2)//3):
            print(3,end=" ")
        print(2)
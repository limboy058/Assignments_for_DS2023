def dfs(now):
    vis[now]=1
    path.append(now)
    
    if now==0:
        paths.append(path.copy())
        path.pop()
        vis[now]=0
        return
        
    else:
        for it in hf[now]:
            if vis[it]==0:
                dfs(it)
        path.pop()
        vis[now]=0
    

# 初始化所有合法点(一岸的情况)
lt=[]
for r in range(0,2,1):
    for c in range(0,2,1):
        for y in range(0,2,1):
            for l in range(0,2,1):
                if (r==0 and not(y==1 and l==1) and not(y==1 and c==1)) or (r==1 and not(y==0 and l==0) and not (y==0 and c==0)):
                    lt.append([r,c,y,l])
#print(lt)

# 初始化所有合法边
hf=[]
for i in range(0,len(lt)):
    line=[]
    for j in range(0,len(lt)):
        check=True
        if lt[i][0]!=lt[j][0]:
            cnt=0
            if lt[i][0]==0:
                for k in range(0,4):
                    if lt[j][k]-lt[i][k]<0:
                        check=False
                    cnt=cnt+lt[j][k]-lt[i][k];
                if cnt>2:
                    check=False
            else:
                for k in range(0,4):
                    if lt[i][k]-lt[j][k]<0:
                        check=False
                    cnt=cnt+lt[i][k]-lt[j][k];
                if cnt>2:
                    check=False
        else:
            check=False
        if check:
            line.append(j)
    hf.append(line)
#print(hf)

# 初始化path及vis
path=[]
vis=[0]*len(lt)
paths=[]

# dfs递归寻找解法
dfs(len(lt)-1)

for i in range(0,len(paths)):
    print("第",i+1,"条路径")
    #print(paths[i])
    for j in range(0,len(paths[i])):
        if lt[paths[i][j]][0]==1:
            print("人",end=" ")
        else:
            print("  ",end=" ")
        if lt[paths[i][j]][1]==1:
            print("菜",end=" ")
        else:
            print("  ",end=" ")
        if lt[paths[i][j]][2]==1:
            print("羊",end=" ")
        else:
            print("  ",end=" ")
        if lt[paths[i][j]][3]==1:
            print("狼",end=" ")
        else:
            print("  ",end=" ")
        print("|     |",end=" ")
        
        if lt[paths[i][j]][0]==0:
            print("人",end=" ")
        else:
            print("  ",end=" ")
        if lt[paths[i][j]][1]==0:
            print("菜",end=" ")
        else:
            print("  ",end=" ")
        if lt[paths[i][j]][2]==0:
            print("羊",end=" ")
        else:
            print("  ",end=" ")
        if lt[paths[i][j]][3]==0:
            print("狼",end=" ")
        else:
            print("  ",end=" ")
        print("")
    print()
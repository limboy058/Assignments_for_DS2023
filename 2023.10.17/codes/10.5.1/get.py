def main():
    f=open(r'2023.10.17\codes\10.5.1\ssby.txt','r')
    mp={}
    for line in f:
        if len(line)>5:
            mark=[',','.','\'',':','?',';','\\','<','>']
            for m in mark:
                line=line.replace(m,'')
            words=line.strip().split(' ')
            for word in words:
                if word.lower() in mp:
                    mp[word.lower()]+=1
                else:
                    mp[word.lower()]=1
    tmp=sorted(mp.items(),key=lambda x:x[1],reverse=True)
    f.close()
    for i in range(0,30,1):
        print(tmp[i])

if __name__ == "__main__":
    main()
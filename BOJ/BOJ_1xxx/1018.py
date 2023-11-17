n, m = map(int, input().split())
lst=[]
lst2=[]
for i in range(n):
    lst.append(input())

for i in range(m-7):
    for j in range(n-7):
        count=0
        for k in range(8):
            for l in range(8):
                if lst[j][i]=='B':
                    if (l+k+i+j)%2==(i+j)%2 and lst[k+j][l+i]=='W':
                        count+=1
                    if (l+k+i+j)%2!=(i+j)%2 and lst[k+j][l+i]=='B':
                        count+=1
                elif lst[j][i]=='W':
                    if (l+k+i+j)%2==(i+j)%2 and lst[k+j][l+i]=='B':
                        count+=1
                    elif (l+k+i+j)%2!=(i+j)%2 and lst[k+j][l+i]=='W':
                        count+=1
        if count>32:
            count=64-count
        lst2.append(count)


print(min(lst2))

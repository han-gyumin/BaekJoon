num=int(input())
lst=list(map(int,input().split()))
lst.sort(reverse=True)
lst2=[]
count=0
for i in lst:
    lst2.append(i-(len(lst)-1-count))
    count+=1
lst2.sort(reverse=True)
print(lst2[0]+1+len(lst2))
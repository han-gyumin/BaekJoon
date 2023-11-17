n, m = map(int,input().split())
lst=[i+1 for i in range(n)]
for i in range(m):
    tmp=0
    a,b=map(int,input().split()) 
    tmp=lst[a-1]
    lst[a-1]=lst[b-1]
    lst[b-1]=tmp   

for i in range(n):
    print(lst[i],end=" ")
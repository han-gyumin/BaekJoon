n=int(input())
lst=list(map(int,input().split()))
lst.sort()
max=lst[-1]
count=0
for i in range(n):
    lst[i]=(lst[i]/max)*100
    count+=lst[i]

print((count)/n)
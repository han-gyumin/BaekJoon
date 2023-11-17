n=int(input())
lst=list(map(int,input().split()))
max=0
for i in lst:
    if i>max:
        max=i
lst.sort(reverse=True)
lst.remove(max)
print(max*len(lst)+sum(lst))
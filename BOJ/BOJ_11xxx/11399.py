num=int(input())
lst=list(map(int,input().split()))
lst.sort()
count=0
output=0

for i in lst:
    count+=i
    output+=count
print(output)
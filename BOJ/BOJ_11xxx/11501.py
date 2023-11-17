import sys
input=sys.stdin.readline
case=int(input())
for _ in range(case):
    n=int(input())
    output=0
    count=0
    lst=list(map(int,input().split()))
    for i in range(len(lst)):
        count+=1
        max=0
        lst2=lst[:]
        lst2.sort(reverse=True)
        for j in range(count,n):
            # print(lst2)
            # print(lst[j])
            # print(lst2[0])
            if lst[j]==lst2[0]:
                max=lst2[0]
                print(lst2[0])
                lst2.pop(0)
                print(lst2[0])
                # print(max)
                break
        if lst[i]<max:
            output+=(max-lst[i])
    print(output)
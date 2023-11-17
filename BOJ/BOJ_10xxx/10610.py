lst=[]
n=input()
count=0
for i in n:
    lst.append(i)
for i in range(len(n)):
    count+=(int(lst[i]))
if "0" not in n or count%3!=0:
    print("-1")
else:
    lst.sort(reverse=True)
    for i in range(len(lst)):
        print(lst[i],end="")
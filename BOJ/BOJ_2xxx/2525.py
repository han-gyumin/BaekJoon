a,b = map(int,input().split())
c=int(input())

if (b+c)>=60 :
    a=(a+((c+b)//60))
    b=((b+c)%60)
else:
    a=a
    b=(b+c)

if a>23:
    a=(a-24)

print(a,b)
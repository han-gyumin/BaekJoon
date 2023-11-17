n=int(input())
num=0
count=0
lst=[]
i=0
while(True):
    if n%5==0 and i==0:
        print(n//5)
        break
    elif n>3:
        if (n-3)%5==0:
            num+=1
            n-=3
            print((n//5)+num)
            break
        else:
            n-=3
            num+=1
    elif n==3:
        print(num+1)
        break
    else:
        print("-1")
        break
    i=+1




    
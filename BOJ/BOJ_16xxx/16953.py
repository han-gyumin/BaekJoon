import sys
input=sys.stdin.readline

a,b=map(int,input().split())
output=1
while(True):
    if b==a:
        break
    elif (b%2!=0 and b%10!=1) or b<a:
        output=-1
        break
    else:
        if b%10==1:
            b=(b//10)
            output+=1
        else:
            b=(b//2)
            output+=1

print(output)
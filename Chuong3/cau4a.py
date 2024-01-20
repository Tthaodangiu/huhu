s=0
n=int(input())
x=1
while s<=n:
    s+=x
    if s>n:
        x-=1
        break
    x+=1
print('So can tim la',x)
a=int(input())
b=int(input())
count=0
i=b-1
while i>a and i<b:
    if i % 3 == 0:
        print(i,end=' ')
        count=count+1
    i=i-1
if count<1:
    print('Notfound')
a=int(input())
b=int(input())
count=0
for i in range(a+1,b-1):
    if i % 3 == 0:
        print(i,end=' ') 
        count = count + 1
if count < 1:
    print('NOT FOUND')


    
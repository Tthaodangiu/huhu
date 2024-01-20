L=[]
n=int(input('n='))
for i in range(n):
    L.append(int(input()))
count=0
for i in L:
    if i>0:
        count+=1
print('SND=',count,sep='')
x=0
m=0
for j in L:
    if j%2==0:
        x=x+j
        m+=1
if m>0:
    TBC=x/m
    print('TBC=',TBC,sep='')
else:
    TBC=0
    print('TBC=',TBC,sep='')


        

        
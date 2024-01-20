def Thayso(L,y,x):
    print('Cau a')
    for i in range(len(L)):
        if L[i]==y:
            L[i]=x
    for i in L:
        print(i ,end=",")
    print(end='\n')
def Delete(L,x):
    print('Cau b')
    while x in L:
        L.remove(x)
    for i in L:
        print(i,end=",")
L = []
for i in range(10):
    n=int(input())
    L=L+[n]
    
x=int(input('x='))
Thayso(L,5,x)
Delete(L,x)

    
    
        
    
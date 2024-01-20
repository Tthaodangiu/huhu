x=int(input('x='))
L=[]
n=int(input('n='))
for i in range(n):
    L.append(int(input()))
def Delete(L,x):
    while x in L:
        L.remove(x)
    print(L)
Delete(L,x)
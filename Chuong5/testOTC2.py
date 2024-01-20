x=int(input('x='))
L=[]
n=int(input('n='))
for i in range(n):
    L.append(int(input()))
def search(L,x):
    for i in range(len(L)):
        if x==L[i]:
            print('Vi tri cua',x,'la',i)
            return i
    return None
var=search(L,x)
print(var)

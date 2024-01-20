x=int(input())
L=[]
n=int(input())
for i in range(n):
    L.append(int(input()))
def search(L,x):
    if x in L:
        i=L.index(x)
        return i
    else:
        return None
var=search(L,x)
print(var)

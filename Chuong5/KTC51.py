def Nhap():
    L=[]
    n=int(input('n='))
    for i in range(n):
        L.append(int(input()))
    x=int(input('x='))
    return L,x
def FirstAndLast(L):
    L2=L.copy()
    n=len(L2)
    del L2[1:n-1]
    print(L2)
def Search(L,x):
    if x in L:
        return True
    else:
        return False
L,x=Nhap()
FirstAndLast(L)
var=Search(L,x)
print(var)



    
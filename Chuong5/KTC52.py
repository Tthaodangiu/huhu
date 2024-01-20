def Nhap():
    L=[]
    n=int(input('n='))
    for i in range(n):
        L.append(int(input()))
    return L
def Search(L):
    min=L[0]
    for i in L:
        if i<min:
            min=i
    max=L[0]
    for i in L:
        if i>max:
            max=i
    return max,min
def Output(max,min):
    print(max,min)
L=Nhap()
max,min=Search(L)
Output(max,min)

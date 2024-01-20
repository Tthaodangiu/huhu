x=int(input('x='))
L=[]
n=int(input('n='))
for i in range(n):
    L.append(int(input()))
def Delete(L,x):
    i = 0
    while i < len(L):
        if L[i] == x:
            L.pop(i)
        else:
            i += 1
    print(L)
Delete(L,x)
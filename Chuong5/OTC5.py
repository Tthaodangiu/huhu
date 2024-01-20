x=int(input())
y=int(input())
L=[]
n=int(input())
for i in range(n):
    L.append(int(input()))
def Replace(L,x,y):
    for i in range(len(L)):
        if L[i]==x:
            L[i]=y
    print(L)
Replace(L,x,y)
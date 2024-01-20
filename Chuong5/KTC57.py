L=[]
n=int(input('n='))
for i in range(n):
    L.append(int(input()))
L.reverse()
for i in range(len(L)):
    for j in range(len(L)):
        if L.count(len(L)-j)>1:
            L.remove(len(L)-j)
L.reverse()
M=L.copy()
for i in M:
    print(i,end=" ")

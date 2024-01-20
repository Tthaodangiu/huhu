L=[]
n=10
for i in range(n):
    L.append(int(input()))
A=L.copy()
for j in range(0,n-1,2):
        temp = L[j]
        L[j] = L[j + 1]
        L[j + 1] = temp
for i in L:
    print(i,end=" ")
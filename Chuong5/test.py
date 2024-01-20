L=[]
n=int(input('n='))
for i in range(n):
    L.append(int(input()))
i = 0
while i < len(L):
    num = L[i]
    j = i + 1
    while j < len(L):
        if L[j] == num:
            L.pop(j)
        else:
            j += 1
    i += 1
M=L.copy()
for i in M:
    print(i,end=" ")
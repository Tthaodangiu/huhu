str = str(input())

L=str.split()
G=[]
for i in range(len(L)):
    if len(L[i]) > 3:
        G.append(L[i])
print(G)
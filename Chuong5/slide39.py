L=[1,2,3,5,5,5,8,9,5]
x=5
i=0

for i in range(len(L)):
    if L[i]==5:
        L[i]=10
print(L)
while x in L:
    L.remove(x)
print(L)
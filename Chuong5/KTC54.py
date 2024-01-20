ListA=[]
n=int(input('n='))
for i in range(n):
    ListA.append(int(input()))
ListA.reverse()
ListB=ListA.copy()
print(ListB)
ListB.sort()
print(ListB)
LA=[]
n=int(input('n='))
for i in range(n):
    LA.append(int(input()))
LA.reverse()
LB=LA.copy()
print(LB)
n = len(LB)
for i in range(1,n-1):
    for j in range(0, n - i ):
        if LB[j] > LB[j + 1]:
            temp = LB[j]
            LB[j] = LB[j + 1]
            LB[j + 1] = temp
print(LB)

L=[]
n=int(input())
for i in range(n):
    L.append(int(input()))
def count(L):
    count=0
    for i in L:
        count+=1
    print(count)
count(L)
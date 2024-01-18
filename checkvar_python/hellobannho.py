a = int(input())
b = int(input())
A=[]
B=[]
G=[]
for i in range(1,a+1):
    if a%i==0:
        A.append(i)
    
for i in range(1,b+1):
    if b%i==0:
        B.append(i)
    
for i in A:
    for j in B:
        if i==j:
            G.append(i)
print(max(G))
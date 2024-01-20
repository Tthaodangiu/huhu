N=int(input())
A=[]
for i in range(0,N):
    n=int(input())
    A.append(n)
List=[]
for i in range(0,N):
    X=[]
    Y=[]
    sumX=0
    sumY=0
    for i in range(0,i):
        X.append(A[i])
        sumX=sum(X)
    for i in range(i+1,N):
        Y.append(A[i])
        sumY=sum(Y)
    List.append(abs(sumX-sumY))
print(min(List))
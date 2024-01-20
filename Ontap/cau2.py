n=int(input())
tong=1
T=0
for i in range(2,n+1):
    n=n-1
    for j in range(2,n):
        tong=tong*i
        T=T+tong
print(tong)
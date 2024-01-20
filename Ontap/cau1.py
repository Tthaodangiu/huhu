n=int(input())
check=1
tong=0
for i in range(2,n+1):
    for j in range(2,n):
        if i % j == 0:
            check=0
    if check == 1:
        tong=tong+i
print(tong)
        
    
            

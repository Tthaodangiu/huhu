n=int(input())
i = 0
for i in range(2,n+1):
    if i%2!=0:
        continue
    print(i,end=" ")
    #Liệt kê số chẵn từ 2 tới đâu đó mà xài for
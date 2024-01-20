n = int(input("n = "))
i=1
for i in range(1,n+1):
    if i%10==0:
        print(i,end= "\n")
    else:
        print(i,end= " ")
ten=[]
soluong=[]
for i in range(4):
    T=input()
    ten=ten+[T]
    S=str(input())
    soluong=soluong+[S]
for i in range(0,4):
    print(ten[i].ljust(15,'.'),end='')
    print(soluong[i].rjust(10))
    
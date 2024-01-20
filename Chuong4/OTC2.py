def SNT(n):
    check=1
    for i in range(2,n):
        if n % i == 0:
            check=0
            break
    if check == 1:
        return True
    else:
        return False
def Dem(n):
    p = 2
    count=0
    while True:
        if SNT(p):
            print(p,end=' ')
            count+=1
        p+=1
        if count>=n:
            break
Dem(n=int(input('n=')))
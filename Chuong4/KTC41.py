def nhap():
    n=int(input('n='))
    return n
def giaithua(n):
    gt=1   
    for i in range(1,n+1):
        gt=gt*i
    return gt
def inkq(kq):
    print(n,'!=',kq,sep='')
n=nhap()
kq=giaithua(n)
inkq(kq)
#Tính giai thừa
        
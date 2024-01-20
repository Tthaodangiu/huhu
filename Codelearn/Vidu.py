def Nhap():
    n=int(input('n='))
    return n
def NhapVaDem(n):
    print('Nhap',n,'so nguyen:')
    sochan=0
    for i in range(1,n+1):
        x=int(input())
        if x % 2 == 0:
            sochan+=1
    return sochan
def InKQ(kq):
    print('Chu so chan la',kq)

n=Nhap()
kq=NhapVaDem(n)
InKQ(kq)

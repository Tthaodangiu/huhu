def is_prime(n):
    if n<=1:
        return False
    check=1
    for i in range(2,n):
        if n%i==0:
            check=0
            break
    if check==1:
        return True
    else:
        return False
    
def Sohople(n): 
        return n<=1
def NhapvaDem():
    print('Nhap day so:')
    S=0
    while True:
        n=int(input())
        
        if Sohople(n):
            break
        elif is_prime(n):
            S+=1
    return S
    
def inkq(kq):
    print('Co',kq,'so nguyen to')

kq=NhapvaDem()   
inkq(kq)
    
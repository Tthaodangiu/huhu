#Xem số nhập vào có phải là SNT không. Nếu có/không thì print 
def Nhap():
        n=int(input('n='))
        return n
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
    
def InKQ(kq):

        if SNT(n):
            print(n,'la so nguyen to')
        else:
            print(n,'khong phai so nguyen to')
            
n=Nhap()
kq=SNT(n)
InKQ(kq)
        
        

    
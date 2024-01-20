def Nhap():
    n=int(input('n='))
    sochan=0
    print('Nhap',n,"so nguyen")
    for i in range(1,n+1): 
        x=int(input())
        if x % 2 == 0:
            sochan+=1
    
    return sochan
    #print('So chu so chan la',sochan)
kq=Nhap()
print('So chu so chan la:',kq)
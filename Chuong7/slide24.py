while True:
    a=input()
    b=input()
    S=0
    if a.isdecimal() and b.isnumeric() :
        S=int(a) + int(b)
        print('a+b=',S,sep='')
        break
    else:
        print('Khong hop le!!!!')
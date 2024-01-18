def Nhap():
    x=float(input('x='))
    y=float(input('y='))
    ch=input('Phep toan:')
    return x,y,ch
def Tinh(x,y,ch):
    if ch=='+':
        print (x,ch,y,'=',x+y,sep='')
    elif ch=='-':
        print (x,ch,y,'=',x-y,sep='')
    elif ch=='*':
        print (x,ch,y,'=',x*y,sep='') 
    elif ch=='/' and y!=0 :  
        print (x,ch,y,'=',x/y,sep='')
    elif ch=='/' and y==0 :
        print('Khong hop le')
    
def Lap():
    while True:
        ct=str(input('Tiep tuc khong:'))
        if ct != 't' and ct!='T':
            Nhap()
            Tinh(x,y,ch)
        else:
            break
    
x,y,ch=Nhap()
Tinh(x,y,ch)
Lap()
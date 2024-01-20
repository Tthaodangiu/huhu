import math
def nhap():
    print('Nhap 3 so nguyen:')
    a=float(input('a='))
    b=float(input('b='))
    c=float(input('c='))
    return a,b,c
def giaipt(a,b,c):
    delta=(b**2 - 4*a*c)
    if delta>=0:
        candelta=math.sqrt(delta)
        x1 =(-b + candelta)/(2*a)                       #Giải phương trình bậc 24
        x2 =(-b - candelta)/(2*a)
        return x1,x2
    elif delta==0:
        x1=(-b/2*a)
        x2=x1
        return x1,x2
    else:
        x1=str('None')
        x2=str('None')
        return x1,x2
    
def inkq(x1,x2):
    if isinstance(x1,float) == True:
        if x1!=x2:
            print('Phuong trinh co hai nghiem')
            print('x1=',x1,sep='')
            print('x2=',x2,sep='')
        else:
            print('Phuong trinh co nghiem kep')
            print('x1=x2=',x1,sep='')
    else:
        print('Phuong trinh vo nghiem')
a,b,c=nhap()
x1,x2=giaipt(a,b,c)
inkq(x1,x2)
        
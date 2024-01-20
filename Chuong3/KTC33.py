x=float(input('x='))
y=float(input('y='))
ch=str(input('Phep toan:'))
if ch == "+":
    
    print(str(x) + "+" + str(y) + "=",round(x+y,1),sep='')
elif ch == "-":
    
    print(str(x) + "-" + str(y) + "=",round(x-y,1),sep='')
elif ch == "*":
    
    print(str(x) + "*" + str(y) + "=",round(x*y,1),sep='')
elif ch == "/" and y !=0 :
    
    print(str(x) + "/" + str(y) + "=",round(x/y,1),sep='')
    if y==0:
        print('Khong hop le')
else:
    print('Khong hop le')
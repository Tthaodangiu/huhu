a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
import math
p=(a+b+c)/2
x=math.sqrt(p*(p-a)*(p-b)*(p-c))
if (a+b)>c and (a+c)>b and (b+c)>a:
    print("Dien tich=",round(x,3),sep='')
else:
    print("Khong hop le")
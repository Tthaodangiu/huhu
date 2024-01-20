a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if (a*a == b*b + c*c) or (b*b == a*a + c*c) or (c*c == a*a + b*b):
    print('Tam giac vuong')
elif (a == b) and (b == c) and (c == a):
    print('Tam giac deu')
elif (a+b<=c) or b+c<=a or a+c<=b:
    print('Khong hop le')
else:
    print("Tam giac loai khac")
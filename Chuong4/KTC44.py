def max3(a, b, c):
    if a>b and a>c:
        return a
    if b>c:
        return b
    else:
        return c
def nhap():
    print('Nhap 3 so nguyen:')
    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))
    return a,b,c
def inkq(max):
    print('So lon nhat la:',max)
a,b,c=nhap()
max=max3(a,b,c)
inkq(max)
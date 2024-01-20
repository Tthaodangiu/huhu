#Tim so lon nhat trong cac so nhap vao
def max3(a, b, c):

    if a>b and a>c:
        return a
    if b>c:
        return b
    else:
        return c

def nhap():
    a = int(input())
    b = int(input())
    c = int(input())
    return a,b,c
def inkq(max):
    print('So lon nhat la',max)
a,b,c=nhap()
max=max3(a,b,c)
inkq(max)

print('Nhap day so:')
lst=[]
while True:
    x=int(input())
    if x==0:
        break
    lst=lst+[x]
n=int(input('n='))
if n in lst:
    print(n,'co ton tai')
else:
    print('khong ton tai')

x=int(input())
y=int(input())
z=int(input())
a=((x*2)+(y*3)+(z*1))/6
if a>=3 and a<5:
    print('Yeu')
elif a>=5 and a<6:
    print('Trung binh')
elif a>=6 and a<7:
    print('Trung binh kha')
elif a>=7 and a<8:
    print('Kha')
elif a>=8 and a<9:
    print('Gioi')
elif a>=9 and a<=10:
    print('Xuat sac')
else:
    print("Kem")
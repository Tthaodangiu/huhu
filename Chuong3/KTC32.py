M1=int(input('M1='))
M2=int(input('M2='))
M3=int(input('M3='))
S=int(input('S='))
if S <= 100:
    sum1=(S*M1)
    print('Phai tra=',sum1,sep='')
elif S>=101 and S<=150:
    sum2=((M1*100)+(S-100)*M2)
    print('Phai tra=',sum2,sep='')
else:
    sum3=((M1*100)+(M2*50)+(S-150)*M3)
    print('Phai tra=',sum3,sep='')
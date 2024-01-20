n=int(input())
t=int(input())
ct=int(input())
if n>100:
    A=((n-100)*25)+(t*15)+(ct*20)
    print(A)
else:
    A=(t*15)+(ct*20)
    print(A)
if n>250:
    B=((n-250)*45)+(t*35)+(ct*25)
    print(B)
else:
    B=(t*35)+(ct*25)
    print(B)
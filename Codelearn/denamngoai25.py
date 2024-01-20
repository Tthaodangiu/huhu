password=str(input())
L=[]
for i in range(0,len(password)):
    if i%2!=0 and i>0:
        if password[i].isnumeric():
            if 1<=int(password[i])<=9:
                L.append(password[i])
if L==[]:
    print('')
else:
    print(''.join(L))
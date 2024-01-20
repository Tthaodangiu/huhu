def password(pw):
    if len(pw) >= 8: 
        L=0 
        U=0 
        N=0 
        for i in range(len(pw)): 
            if pw[i].islower(): 
                L += 1
            elif pw[i].isupper(): 
                U += 1
            elif pw[i].isalnum():
                N = N + 1
        if N>0 and L>0 and U>0:
            return True
        else:
            return False
    else:
        return False
e=password(pw=input())
if e==True:
    print('Hop le')
else:
    while e==False:
        print('Khong hop le')
        e=password(pw=input())
    else:
        print('Hop le')
    
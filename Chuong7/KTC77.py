i=input()
n=i.split(', Email:')
if len(n[1])>0:
    email = n[1][1:]
    print('Email:', email)
    
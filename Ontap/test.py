L=[]
while True:
    n=input()
    if n not in L:
        L=L+[n]
    if n=='':
        break
print(L)
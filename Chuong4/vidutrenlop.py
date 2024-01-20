def max(a,b,c=None):
    if c==None:
        max=a
        if max < b:
            max=b
    else:
        max=a
        if max<b:
            max=b
        if max<c:
            max=c
    print('So lon nhat la',max)
max(5,10,15)
max(5,10)
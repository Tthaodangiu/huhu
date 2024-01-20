n=input()
w=n.split(',')
c=''
for i in range(len(w)):
    if int(w[i],2) % 3 == 0:
        c +=  w[i] + ','
c = c[0:len(c)-1]
m=''.join(c)
print(m)
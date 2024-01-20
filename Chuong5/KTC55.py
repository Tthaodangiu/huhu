L=[]
n=int(input('n='))
for i in range(n):
    L.append(int(input()))
S=0
for i in range(n):
        if i%2!=0:
            S=S+L[i]
print('Tong=',S,sep='')
  
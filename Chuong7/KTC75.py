n=str(input())
w=n.split()
x=int(input())
for i in range(len(w)):
    if x == int(w[i]):
        print(i+1)
if x not in w:
    print('0')
    
    

L = [ [x,x+1,x+2] for x in range(1,13,3) ]
print(L)
def Thayso(L):
    L = [ [x,x+1,x+2] for x in range(1,13,3) ]
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] % 2 == 0:
                L[i][j]="x"

    print(L)
Thayso(L)
            
    
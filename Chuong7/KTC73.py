pw=str(input())
def KT(pw):
    chuthuong=0
    chuhoa=0
    so=0
    kytu=['$', '#', '@']
    kt=0
    if 6<= len(pw) <= 17:
        for i in pw:
            if i.islower():
                chuthuong+=1
            elif '0'<= i <= '9':
                so+=1
            elif i.isupper():
                chuhoa+=1
            elif i in kytu:
                kt+=1
        if chuthuong>=1 and chuhoa>=1 and so>=1 and kt>=1:
            return True
        else:
            return False
var=KT(pw)
print(var)
                    

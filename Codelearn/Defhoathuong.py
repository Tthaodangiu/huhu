#dem so chu hoa va chu thuong
def show(s):
    chuhoa=0
    chuthuong=0
    for i in s:
        if i.isupper():
            chuthuong+=1
        
        if i.islower():
            chuhoa+=1
        
    print('Given string',s)
    print('Number of uppercase letters:',chuthuong)
    print("Number of lowercase letters:",chuhoa)

s = str(input())
show(s)
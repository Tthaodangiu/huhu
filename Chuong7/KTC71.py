pw=str(input())
chuhoa=0
chuthuong=0
so=0
for i in pw:
    if i.isupper():
        chuhoa += 1
    elif i.islower():
        chuthuong+=1
    elif '0'<= i <= '9':
        so+=1
kytu=len(pw)-(chuhoa+chuthuong+so)

print('In hoa:',chuhoa)
print('In thuong:',chuthuong)
print('Chu so:',so)
print('Ky tu:',kytu)
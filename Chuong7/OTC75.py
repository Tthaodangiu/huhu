pw=str(input())
chu=0
so=0
for i in pw:
    if i.isalpha():
        chu += 1
    elif '0'<= i <= '9':
        so+=1
print('Chu cai:',chu)
print('Chu so:',so)
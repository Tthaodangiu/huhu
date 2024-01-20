str=input()
ch=input()
n=0
for i in str:
    if i.lower() == ch.lower():
        n+=1
print('Number of character n is:',n)

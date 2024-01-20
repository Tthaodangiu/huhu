text = int(input())

for i in range(len(text)):
    char = text[i]
    result=result+char
    if char==9:
        print('YES')
    else:
        print('NO')
            
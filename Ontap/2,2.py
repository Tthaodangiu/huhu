total = 0
while True:
    numbers = input().split() 
    for number in numbers:
        if number == 'Q': 
            break
        if '.' not in number and '-' not in number: 
            total +=int(number) 
    if number == 'Q': 
        break
print(total)
#Tính tổng các số nguyên dương nếu gặp Q thì dừng
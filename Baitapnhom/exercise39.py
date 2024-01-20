n=int(input('Enter Decibel level here: '))
if n==130:
    print(n,'is Jackhammer')
elif 106<n<130:
    print(n,'is between Jackhammer and Gas lawnmower')
elif n==106:
    print(n,'is Gas lawnmower')
elif 70<n<106:
    print(n,'is between Gas lawnmower and Alarm clock')
elif n==70:
    print(n,'is Alarm clock')
elif 40<n<70:
    print(n,'is between Alarm clock and Quiet room')
elif n==40:
    print(n,'is Quiet room')
else:
    print('No information')
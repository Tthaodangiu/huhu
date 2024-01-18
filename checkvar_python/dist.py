import math
sum = 0
x = str(input("x = "))
while True:
    if x != "":
        x = int(x)
        y = int(input("y = "))
        p1 = x
        p2 = y
        temp1 = x
        temp2 = y
        x = str(input("x = "))
        while x != "":
            x = int(x)
            y = int(input("y = "))
            dist = math.sqrt((x - temp1)*(x - temp1) + (y - temp2)*(y - temp2))
            sum = sum + dist
            temp1 = x
            temp2 = y
            x = str(input("x = "))
        else:
            dist = math.sqrt((temp1 - p1)*(temp1 - p1) + (temp2 - p2)*(temp2 - p2))
            sum = sum + dist
        print(sum)
    else:
        break

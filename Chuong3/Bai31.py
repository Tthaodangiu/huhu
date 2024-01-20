a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
max = a
if b > max:
    max = b
    if c > max:
        max = c
if c > max :
    max = c
min = c
if a < min:
    min = a
    if b < min:
        min = b
if b < min:
    min = b
print("SLN=",max,sep='')
print("SBN=",min,sep='')
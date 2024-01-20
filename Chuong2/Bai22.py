a=int(input("Nhap Gia niem yet: "))
b=int(input("Nhap Chiet khau: "))
VAT=((a - b) * 0.01)
print("Gia ban: " + str(a - b + VAT))
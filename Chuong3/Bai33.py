a = int(input("Tieu thu="))
if a <= 100:
    sum1 = round(a*550*1.1,1)
    print("Phai tra=", sum1, sep='')
elif a >100 and a <= 150:
    sum2 = round((100*550 + ((a-100)*750))*1.1,1)
    print("Phai tra=", sum2,sep='')
elif a>150 and a<200:
    sum3 = round((100*550 + ((50)*750) + ((a-150)*950))*1.1,1)
    print("Phai tra=", sum3,sep='')
else:
    sum4 = round((100*550 + ((50)*750) + ((50)*950) + ((a-200)*1350))*1.1,1)
    print("Phai tra=", sum4,sep='')
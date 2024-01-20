number = int(input("Nhập một số nguyên: "))
if number <= 1:
    print(number,"không phải số nguyên tố. Số nguyên tố gần nhất là ", 2)
elif number == 2 or number == 3:
    print(number,"La so nguyen to")
else:
    check = 1
    for i in range(2, int(number)):
        if number % i == 0:
            check = 0
        else:
            check = 1
        if check == 0:
            break
    print(number,"là số nguyên tố.")
if check == 0:
    check_lower = 0
    lower_prime = number - 1
    while check == 0:
        for i in range(2, int(lower_prime)):
            if lower_prime % i == 0:
                check_lower = 0
            else:
                check_lower = 1
            if check_lower == 0:
                break
        if check_lower == 1:
            break
        lower_prime -= 1
    upper_prime = number + 1
    check_upper = 0
    while check_upper == 0:
        for i in range(2, int(upper_prime)):
            if upper_prime % i == 0:
                check_upper = 0
            else:
                check_upper = 1
            if check_upper == 0:
                break
        if check_upper == 1:
            break
        upper_prime += 1

    if abs(number - lower_prime) <= abs(number - upper_prime):
        nearest_prime = lower_prime
    else:
        nearest_prime = upper_prime

    print(number,"không phải số nguyên tố. Số nguyên tố gần nhất là ", nearest_prime)
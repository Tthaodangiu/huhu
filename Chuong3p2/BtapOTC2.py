# Nhập số nguyên từ bàn phím
n = int(input("Nhập một số nguyên từ 2 đến 100: "))

# Kiểm tra điều kiện 2 <= n <= 100
if 2 <= n <= 100:
    # Kiểm tra n có phải là số nguyên tố hay không
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    
    # In kết quả
    if is_prime:
        print(n, "là số nguyên tố.")
    else:
        print(n, "không là số nguyên tố.")
else:
    print("Số bạn nhập không nằm trong khoảng từ 2 đến 100.")

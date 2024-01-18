def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_prime_numbers(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num, end=" ")
            count += 1
        num += 1

try:
    n = int(input("n = "))
    if n <= 0:
        print("Vui lòng nhập số nguyên dương lớn hơn 0.")
    else:
        print_prime_numbers(n)
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")

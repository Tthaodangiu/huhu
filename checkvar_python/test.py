def convert_to_decimal(number, base):
    decimal = 0
    power = 0
    while number > 0:
        digit = number % 10
        decimal += digit * (base ** power)
        number //= 10
        power += 1
    return decimal

def subtract_in_base(num1, num2, base):
    # Chuyển đổi số về hệ cơ số 10
    decimal_num1 = convert_to_decimal(num1, base)
    decimal_num2 = convert_to_decimal(num2, base)
    
    # Thực hiện phép trừ trong hệ cơ số 10
    result_decimal = decimal_num1 - decimal_num2
    
    # Chuyển đổi kết quả về hệ cơ số ban đầu
    result_base = ""
    while result_decimal > 0:
        remainder = result_decimal % base
        result_base = str(remainder) + result_base
        result_decimal //= base
    
    return result_base if result_base else "0"

num1 = int(input("n1 = "))
num2 = int(input("n2 = "))
base = int(input("base = "))

result = subtract_in_base(num1, num2, base)
print(f"Kết quả: {result}")

def search(L, x):
    """
    Tìm x trong List L, trả về index của x nếu tìm thấy, ngược lại trả về None.
    """
    try:
        index_of_x = L.index(x)
        return index_of_x
    except ValueError:
        return None
# Nhập số nguyên x từ người dùng
x = int(input("Nhập số nguyên x: "))

# Nhập số nguyên n từ người dùng
n = int(input("Nhập số lượng phần tử trong danh sách n: "))

# Nhập n số nguyên và lưu vào danh sách L
L = []
for i in range(n):
    element = int(input(f"Nhập phần tử thứ {i + 1}: "))
    L.append(element)

# Gọi hàm search và in kết quả
result = search(L, x)
if result is not None:
    print(f"Số {x} được tìm thấy ở index {result}.")
else:
    print(f"Số {x} không tồn tại trong danh sách.")

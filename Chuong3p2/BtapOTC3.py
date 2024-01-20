# Nhập số nguyên dương từ bàn phím và kiểm tra giá trị
while True:
    try:
        n = int(input("n="))
        if 0 <= n <= 9999:
            break
        else:
            print("Số bạn nhập không hợp lệ.")
    except ValueError:
        print("Vui lòng nhập một số nguyên dương hợp lệ.")

# Chuyển số nguyên dương thành chuỗi và đếm số chữ số
so_chu_so = len(str(n))

print( n,'co', so_chu_so ,'chu so')
#Đếm số chữu số của 1 số
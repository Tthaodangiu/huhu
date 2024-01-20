n = int(input("n="))

for i in range(1, n + 1):
    # Sử dụng end=" " để ngăn cách các số bằng một dấu cách thay vì xuống dòng mới
    print(*range(1, n + 1), end=" ")
    print()  # Xuống dòng sau khi in xong mỗi dòng
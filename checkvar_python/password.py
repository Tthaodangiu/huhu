def password(pw):
    if len(pw) > 7: # Kiểm tra xem độ dài của pass có đủ không
        count_LowerCase = 0 # Tạo biến đếm chữ thường
        count_UpperCase = 0 # Tạo biến đếm chữ hoa
        count_Number = 0 # Tạo biến đếm số
        for i in range(len(pw)): # Duyệt chuỗi kí tự
            if 'a' <= pw[i] <= 'z': # Xét nếu là chữ thường thì +1 vào biến đếm chữ thường
                count_LowerCase += 1
            elif 'A' <= pw[i] <= 'Z': # Xét nếu là chữ hoa thì +1 vào biến đếm chữ hoa
                count_UpperCase += 1
            else:
                try: # Sử dụng chức năng tìm kiếm ngoại lệ để kiểm tra kí tự có là số nguyên hay không
                    int(pw[i]) # Sử dụng cách chuyển đổi kiểu dữ liệu từ kí tự thành kiểu số nguyên
                               # Nếu kí tự là số nguyên thì sẽ chuyển đổi thành công mà không gặp lỗi
                               # Khi đổi thành công, tức là try hợp lệ đồng nghĩa với việc đây pw[i] là số, do đó +1 vào biến đếm số
                    count_Number += 1
                except ValueError: # Ở đây, ValueError nghĩa là lỗi giá trị, lỗi này xuất hiện khi pw[i] không phải là số nguyên
                    count_Number = count_Number # Khi pw[i] không phải là số thì ta giữ nguyên biến đếm số 
        if count_Number > 0 and count_LowerCase > 0 and count_UpperCase > 0: # Nếu cả 3 biến đếm cùng lớn hơn 0, tức là cả 3 loại kí tự 
                                                                             # đều xuất hiện ít nhất một lần để thỏa mãn đề bài
            return 1
        else:
            return 0
    else:
        return 0
etc = password(pw = input())
if etc == 1:
    print("Hop le")
else:
    while etc == 0:
        print("Khong hop le")
        etc = password(pw = input())
    else:
        print("Hop le")
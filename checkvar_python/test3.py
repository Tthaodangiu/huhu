def clean_string(input_str):
    # Chuyển tất cả các ký tự trong chuỗi thành chữ thường
    input_str = input_str.lower()

    # Chuyển ký tự đầu tiên của chuỗi thành chữ hoa
    input_str = input_str.capitalize()

    # Tách từng từ trong chuỗi
    words = input_str.split()

    # Xây dựng chuỗi mới sau khi làm sạch
    clean_text = ""
    for idx, word in enumerate(words):
        # Xử lý các từ đầu tiên và các từ không phải dấu câu
        if idx == 0 or word[-1] in [',', ';', ':', '.']:
            clean_text += word
        else:
            clean_text += " " + word

    return clean_text


# Nhập chuỗi từ người dùng
input_string = input("Nhập vào chuỗi: ")

# Làm sạch chuỗi và in ra kết quả
result = clean_string(input_string)
print("Output:", result)

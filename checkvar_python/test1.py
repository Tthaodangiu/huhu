input_string = input()
input_string = input_string.lower()
words = input_string.split()
words[0] = words[0].capitalize()
clean_text = ""

for i in range(len(words)):
    if i == 0:
        clean_text += words[i]
    else:
        # Kiểm tra ký tự đầu của từ có phải là dấu câu không
        if words[i][0] in [',', ';', ':', '.']:
            clean_text += words[i][0]  # Thêm dấu câu vào chuỗi kết quả
            for j in range(1, len(words[i])):
                # Nếu ký tự tiếp theo cũng là dấu câu, chèn khoảng trắng trước nó
                if words[i][j] in [',', ';', ':', '.']:
                    clean_text += " " + words[i][j] + " "
                else:
                    clean_text += words[i][j]  # Nếu không phải dấu câu, thêm ký tự vào chuỗi kết quả
        else:
            clean_text += " " + words[i]  # Nếu từ không bắt đầu bằng dấu câu, thêm từ vào chuỗi kết quả

print(clean_text)

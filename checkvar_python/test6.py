input_string = input("Họ tên, Email: email@... \n")

info = input_string.split(", Email:")

if len(info[1]) > 0:
    email = info[1][1:]
    print("Email:", email)

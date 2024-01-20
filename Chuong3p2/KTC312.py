def encode_number(n):
  
    encoding_dict = {
        '0': 'A',
        '1': 'B',
        '2': 'C',
        '3': 'D',
        '4': 'E',
        '5': 'F',
        '6': 'G',
        '7': 'H',
        '8': 'K',
        '9': 'L'
    }

   
    n_str = str(n)

    
    encoded_str = ''
    for digit in n_str:
        if digit in encoding_dict:
            encoded_str += encoding_dict[digit]

    return encoded_str


n = int(input())


if n < 0 or n > 9999:
    print("Số nguyên không hợp lệ!")
else:
   
    encoded_number = encode_number(n)
    print(encoded_number)
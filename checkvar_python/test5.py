text = '''--Người---đâu-gặp---gỡ-làm-chi--- 
        Trăm----năm-biết-có---duyên---gì--hay--không. 
        Ngổn-ngang---trăm-mối---bên---lòng---- 
        Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình.'''

cau = text.split()
print(cau)
process_text = ''

for tu in cau:
    word = tu.split('-')
    print(word)
    for i in range(len(word)):
        if len(word[i]) > 0:
            if word[i].istitle():
                process_text = process_text[:-1]
                process_text += '\n' + word[i] + ' ' 
            else:
                process_text += word[i] + ' ' 
print(process_text[1:])

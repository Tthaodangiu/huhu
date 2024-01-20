t = '''--Người---đâu-gặp---gỡ-làm-chi--- 
        Trăm----năm-biết-có---duyên---gì--hay--không. 
        Ngổn-ngang---trăm-mối---bên---lòng---- 
        Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình.'''

cau = t.split(" ")
print(cau)
p = ''
for tu in cau:
    w = tu.split('-')
    for i in range(len(w)):
        if len(w[i]) > 0:
            if w[i].istitle():
                p += '\n' + w[i] + ' '
            else:
                p += w[i] + ' '
print(p[1:])
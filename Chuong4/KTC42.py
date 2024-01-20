def nhap(n=int(input('n='))):
    for i in range(2,n+1,2):  
        print(i,end=' ')       
def inkq():
    while True:
        print(end='\n')
        x=str(input('Tiep tuc khong?'))                     #Liệt kê số chẵn theo hàng ngang rồi hỏi lại tiếp tục k
        if x!='k' and x!='K':
            #n=int(input('n='))
            nhap(n=int(input('n=')))
        else:
            break  

nhap()
inkq()

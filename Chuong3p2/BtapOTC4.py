x=float(input('x='))
y=float(input('y='))
ch=input('Phep toan:')
if ch=='+':
        print (x,ch,y,'=',x+y,sep='')
elif ch=='-':
        print (x,ch,y,'=',x-y,sep='')
elif ch=='*':
        print (x,ch,y,'=',x*y,sep='') 
elif ch=='/' and y!=0 :  
        print (x,ch,y,'=',x/y,sep='')
elif ch=='/' and y==0 :
        print('Khong hop le')
while (True):
    ct=str(input('Tiep tuc:'))
    
    if ct != "t" and ct != "T":
        x=float(input('x='))
        y=float(input('y='))
        ch=input('Phep toan:')
        if ch=='+':
            print (x,ch,y,'=',x+y,sep='')
        elif ch=='-':
            print (x,ch,y,'=',x-y,sep='')
        elif ch=='*':
            print (x,ch,y,'=',x*y,sep='') 
        elif ch=='/' and y!=0 :  
            print (x,ch,y,'=',x/y,sep='')
        elif ch=='/' and y==0 :
            print('Khong hop le')
    else: break
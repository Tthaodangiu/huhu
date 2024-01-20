N=int(input())
sum=0
k=0
for i in range(0,N):
    string=str(input())
    if string.isnumeric():
        sum+=int(string)
        k=k+1
if k==0 or sum==0:
    print('0')
else:
    print(sum/k)
#Tính trung bình các số

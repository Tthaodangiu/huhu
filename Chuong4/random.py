import random
def Human():
    while True:
        n=int(input())
        if 0<n<3:
            print('Nguoi",n')
        else:
            break
def Computer():
    m=random.randint(1,3)
    print('May',m)
    return m
def kiem_tra_thang_thua_nguoi_may(n, m):
    if n == m:
        return "Hòa"
    elif (n == 1 and m== 3) or (n == 2 and m == 1) or (n == 3 and m== 2):
        return "Người thắng"
    else:
        return "Máy thắng"
def main():
    while True:
        n= Human()
        if n == 0:
            print("Kết thúc chương trình.")
            break
main()
matrix = []
m = int(input("Nhap so dong: "))
n = int(input("Nhap so cot: "))
for i in range(m):
    row = []
    for j in range(n):
        row += [int(input())]
    matrix += [row]  
for row in matrix:
    print(row)
for i in range(len(matrix)):
    for j in range(len(row)):
        if matrix[i][j] % 2 == 0:
            matrix[i][j] = 'x'
for row in matrix:
    print(row)
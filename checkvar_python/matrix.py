matrix = []
m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))
for i in range(m):
    row = []
    for j in range(n):
        row += [int(input(f"Dòng {i+1} cột {j+1}: "))]
    matrix += [row]  
for row in matrix:
    print(row)
for i in range(len(matrix)):
    for j in range(len(row)):
        if matrix[i][j] % 2 == 0:
            matrix[i][j] = 'x'
for row in matrix:
    print(row)
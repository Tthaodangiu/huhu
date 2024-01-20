def xoa(lst,i):
    while i in lst:
        lst.remove(i)
L = [1, 2, 3, 5, 5, 5, 8, 9, 5]
xoa(L, 5)
print(L)
n = str(input())
w = n.split(',')
i = 0
while i < len(w):
    num = w[i]
    j = i + 1
    while j < len(w):
        if w[j] == num:
            del(w[j])
        else:
            j += 1
    i += 1
w.sort()
m=','.join(w)
print(m)

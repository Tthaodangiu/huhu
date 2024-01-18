def remove_all_values(lst, value):
    while value in lst:
        lst.remove(value)

L = [1, 2, 3, 5, 5, 5, 8, 9, 5]
remove_all_values(L, 5)

print("List after removing all occurrences of 5:", L)
def replace_elements(lst, target_value, replacement_value):
    for i in range(len(lst)):
        if lst[i] == target_value:
            lst[i] = replacement_value

def remove_elements(lst, value):
    while value in lst: 
        lst.remove(value)

L = []
for i in range(10):
    number = int(input(f"Enter integer number {i + 1}: "))
    L.append(number)

print("List before: ",L)

x = int(input("Enter x: "))

replace_elements(L, 5, x)
print("List after replacement by x: ",L)

remove_elements(L, x)
print("List after remove x: ",L)
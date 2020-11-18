#num_list = [1, 2, 2, 4, 5]
num_list=[1, 1, 0, 2, 0, 0, 8, 3, 0, 2, 5, 0, 2, 6]
print(num_list)

for item in num_list:
    if item == 0:
        num_list.remove(item)
    else:
        print(item)

print(num_list)

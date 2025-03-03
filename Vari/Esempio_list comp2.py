num_list = [1, -2, -3, -8.9, -3, 1, 5, -9]
new_list = [abs(n) for n in num_list if num_list.count(n) == 1]
print(new_list)

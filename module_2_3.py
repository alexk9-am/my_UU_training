my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = len(my_list)
i = 0
while i < count:
    if my_list[i] >= 0:
        if my_list[i] > 0:
            print(my_list[i])
        i = i + 1
        continue
    else:
        break


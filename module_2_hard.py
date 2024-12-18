def number_pair(num):                   # Функция формирования списка кратных пар чисел
    pair_list = []                      # Список пар, для которых, число num кратно сумма чисел пары
    for i in range(1, num):             # Цикл по первому числу пары
        j = i + 1                       # Начальное значение второго числа пары
        while i + j <= num:             # Цикл по второму числу пары. Цикл работает пока сумма чисел пары i + j
            if num % (i + j) == 0:      # не превысит само число num, т.к. в этом случае число num
                pair_list.append(i)     # однозначно будет не кратно сумме чисел пары
                pair_list.append(j)     # Цикл с начальным значением j = i + 1 исключает формирование
#            print(i, ' ', j)           # "зеркальных" пар чисел i + j и j + i
            j = j + 1
    return pair_list


for num in range(3, 21):                # Цикл по значениям первого поля "замка ловушки"
    pair_string = ''                    # Начальное значения строки пароля
    list_pair = number_pair(num)        # Вызов функции формирования списка кратных пар чисел для каждого num
    for j in range(len(list_pair)):     # Цикл для преобразование списка кратных пар чисел в строку
        pair_string += str(list_pair[j])
    print(num, ' - ', pair_string)      # Вывод результата на консоль




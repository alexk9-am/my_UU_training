def count_calls():
    global calls
    calls += 1
    return


def string_info(my_string):
    count_calls()
    list_1 = []
    list_1.append(len(my_string))
    list_1.append(my_string.upper())
    list_1.append(my_string.lower())
    tuple_1 = tuple(list_1)
    return tuple_1


def is_contains(string_arg, list_arg):
    count_calls()
    result_fun = False
    string_arg = string_arg.upper()
    for i in range(len(list_arg)):
        list_arg[i] = list_arg[i].upper()
        if string_arg == list_arg[i]:
            result_fun = True
            break
    return result_fun


calls = 0
print(string_info("Обучение"))
print(string_info("авто" + "Машина"))
print(is_contains('Urban', ['uRban', 'BaNaN', 'uraBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('кокос', ['KOKOC', 'socks', 'crocus', 'Кокосанка']))
print(calls)

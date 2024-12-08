# Решение - вариант № 1
print("Вариант № 1")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    is_prime = True
    if i == 1:              # игнорируем проверку числа i из списка numbers
        continue
    for j in range(i):      # при range(i) исключаем проверку деления числа i на само себя
        if j > 1:           # исключаем проверку деления числа i на 0 и 1
            if i % j == 0:
                is_prime = False
                break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)


# Решение - вариант № 2
print("Вариант № 2")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    integer_divizors = []   # список целочисленных делителей числа i
    if i == 1:              # игнорируем проверку числа i из списка numbers
        continue
    for j in range(i):      # при range(i) исключаем проверку деления числа i на само себя
        if j > 1:           # исключаем проверку деления числа i на 0 и 1
            if i % j == 0:
                integer_divizors.append(j)
    if len(integer_divizors) == 0:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)
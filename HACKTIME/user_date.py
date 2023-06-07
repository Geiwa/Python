numbers = input("Введите 5 чисел через пробел: ").split()

number_set = set(map(int, numbers))

min_number = min(number_set)

print("Самое маленькое число: ", min_number)

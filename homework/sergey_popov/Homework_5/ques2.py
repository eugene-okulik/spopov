# 1-я строка
line = "результат операции: 42"
colon_index = line.index(':')
number_str = line[colon_index + 1:]
number = int(number_str)
print(number + 10)

# 2-я строка
line = "результат операции: 514"
colon_index = line.index(':')
number_str = line[colon_index + 1:]
number = int(number_str)
print(number + 10)

# 3-я строка
line = "результат работы программы: 9"
colon_index = line.index(':')
number_str = line[colon_index + 1:]
number = int(number_str)
print(number + 10)

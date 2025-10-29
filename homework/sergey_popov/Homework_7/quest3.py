def process_result(text):
    return int(text.split()[-1]) + 10


lines = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

for line in lines:
    print(process_result(line))

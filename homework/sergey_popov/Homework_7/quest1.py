secret_number = 7  
guess = None

while guess != secret_number:
    guess = int(input("Угадайте число от 1 до 10: "))
    if guess != secret_number:
        print("Попробуйте снова!")

print("Поздравляю! Вы угадали!")

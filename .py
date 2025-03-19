# Завдання 1: Перетворення рядка в число та зворотне перетворення
# Отримуємо рядок, що містить число
num_str = input("Введіть число: ")

# Конвертуємо у число (int або float)
if '.' in num_str:
    num = float(num_str)
else:
    num = int(num_str)

# Виконуємо арифметичну операцію (додаємо 10)
result = num + 10

# Перетворюємо результат назад у рядок та виводимо
print("Результат: " + str(result))

# Завдання 2: Арифметичні операції з введеними даними
# Отримуємо два числа у вигляді рядків
num1_str = input("Введіть перше число: ")
num2_str = input("Введіть друге число: ")

# Конвертуємо у числові типи
num1 = float(num1_str)
num2 = float(num2_str)

# Виконуємо арифметичні операції
sum_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2 if num2 != 0 else "Ділення на нуль неможливе"

# Виводимо результати
print(f"Сума: {sum_result}")
print(f"Різниця: {sub_result}")
print(f"Добуток: {mul_result}")
print(f"Частка: {div_result}")

# Завдання 3: Конвертація списку рядків у список чисел
# Отримуємо рядок із числами, розділеними комами
num_list_str = input("Введіть числа, розділені комами: ")

# Розбиваємо рядок у список та конвертуємо у числа
num_list = [float(num.strip()) for num in num_list_str.split(",")]

# Обчислюємо суму та середнє значення
sum_numbers = sum(num_list)
avg_numbers = sum_numbers / len(num_list)

# Виводимо результати
print(f"Сума чисел: {sum_numbers}")
print(f"Середнє значення: {avg_numbers}")

# Завдання 4: Форматування числових значень
# Отримуємо число з плаваючою комою
float_num = float(input("Введіть число з плаваючою комою: "))

# Форматуємо число з двома десятковими знаками
formatted_num = f"{float_num:.2f}"

# Виводимо відформатований результат
print(f"Відформатоване число: {formatted_num}")

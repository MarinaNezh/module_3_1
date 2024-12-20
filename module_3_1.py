# Переменная
calls = 0

# Функция 1
def count_calls():
    global calls
    calls += 1

# Функция 2
def string_info(string):
    count_calls()
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return length, upper_case, lower_case

# Функция 3
def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [item.lower() for item in list_to_search]

# Вызов функций
result1 = string_info("Hello World")
result2 = string_info("Hello Cat")
result3 = is_contains("Chocolate", ["CITY", "town", "chocolate", "village"])
result4 = is_contains("Dog", ["Cow", "cat", "bird"])

# Результаты
print(result1)
print(result2)
print(result3)
print(result4)

# Количество вызовов функций
print("Количество вызовов функций:", calls)


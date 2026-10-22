print("Вітаю в розумному калькуляторі!")
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
operation = input("Що зробити? Введіть + або -: ")

if operation == "+":
    result = a + b
    print("Сума дорівнює:", result)
elif operation == "-":
    result = a - b
    print("Різниця дорівнює:", result)
else:
    print("Помилка! Я не знаю такої операції.")

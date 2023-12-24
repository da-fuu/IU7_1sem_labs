# Жаринов Михаил Андреевич ИУ7-12Б
# Программа для определения принадлежности точки графику

# Ввод данных
x, y = map(int, input('Введите х и у через пробел: ').split())

# Блок вычислений
ans = 'Точка не принадлежит бабочке'
if -9 <= x <= 8 and 7 * (x + 8) ** 2 + 1 <= y <= -(x + 9) ** 2 / 8 + 8:  # Верхнее левое крыло
    ans = 'Точка принадлежит бабочке'
if -8 <= x <= -1 and (x + 1) ** 2 / 49 <= y <= -(x + 9) ** 2 / 8 + 8:
    ans = 'Точка принадлежит бабочке'
if -8 <= x <= -2 and (x + 5) ** 2 / 3 - 7 <= y <= -(x ** 2) / 16:  # Нижнее левое крыло
    ans = 'Точка принадлежит бабочке'
if -2 <= x <= -1 and -2 * (x + 1) ** 2 - 2 <= y <= -(x ** 2) / 16:
    ans = 'Точка принадлежит бабочке'
if -2 <= x <= 0 and y == -3 * x / 2 + 2:  # Левый усик
    ans = 'Точка принадлежит бабочке'
if 8 <= x <= 9 and 7 * (x - 8) ** 2 + 1 <= y <= -(x - 9) ** 2 / 8 + 8:  # Верхнее правое крыло
    ans = 'Точка принадлежит бабочке'
if 1 <= x <= 8 and (x - 1) ** 2 / 49 <= y <= -(x - 9) ** 2 / 8 + 8:
    ans = 'Точка принадлежит бабочке'
if 2 <= x <= 8 and (x - 5) ** 2 / 3 - 7 <= y <= -(x ** 2) / 16:  # Нижнее правое крыло
    ans = 'Точка принадлежит бабочке'
if 1 <= x <= 2 and -2 * (x - 1) ** 2 - 2 <= y <= -(x ** 2) / 16:
    ans = 'Точка принадлежит бабочке'
if 0 <= x <= 2 and y == 3 * x / 2 + 2:  # Правый усик
    ans = 'Точка принадлежит бабочке'
if -1 <= x <= 1 and 4 * x ** 2 - 6 <= y <= -4 * x ** 2 + 2:  # Брюшко
    ans = 'Точка принадлежит бабочке'

# Блок вывода
print(ans)
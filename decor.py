def debug(func):
    def wrapper(*args):
        print(f'Имя функции: {func.__name__} \nпараметры функции: {args} \nвозвращаемое значение: {func(*args)}')

    return wrapper


@debug
def func_1(num1, num2, num3):
    return num1 + num2


f = func_1(2, 3, 4)

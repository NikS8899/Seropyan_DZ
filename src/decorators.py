from src.widget import get_data


def log(filename=None):
    """Декоратор для логирования вызовов функций. Параметры:
    filename (str): Имя файла для записи логов. Если None, логи выводятся в консоль.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename is None:
                    print(f"{func.__name__} ok\n")
                    return result
                else:
                    with open(filename, "a+") as file:
                        file.write(f"{func.__name__} ok\n")
                    return result
            except Exception as e:
                if filename is None:
                    print(f"{func.__name__} error: {e} input {args} \n")
                else:
                    with open(filename, "a+") as file:
                        file.write(f"{func.__name__} error: {e} input {args} \n")

        return wrapper

    return decorator


@log()
def sqr_func(x):
    return x / x


sqr_func(0)

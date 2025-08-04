from datetime import datetime
from functools import wraps


def log(filename=None):
    """Декоратор для логирования"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            start_message = f"[{timestamp}] Start: {func_name}"
            write_log(start_message, filename)

            try:
                result = func(*args, **kwargs)
                log_message = f"[{timestamp}] Stop: {func_name} ok\n"
                write_log(log_message, filename)
                return result

            except Exception as e:
                error_message = (
                    f"[{timestamp}] Stop: {func_name} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                )
                write_log(error_message, filename)

                raise

        return wrapper

    return decorator


def write_log(message, filename):
    """Вспомогательная функция для записи и вывода"""

    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message)
    else:
        print(message)

import logging
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(message)s')
def log_args(func):
    def wrapper(*args):
        result = func(*args)
        logging.info(f"Аргументы: {args}, Результат: {result}")
        return result
    return wrapper
@log_args
def add(a, b):
    return a + b
add(2, 3)
add(5, 7)

import logging

# Logger setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

# Decorator definition
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        func_name = f"function: {func.__name__}"
        pos_args = f"positional parameters: {args if args else 'none'}"
        kw_args = f"keyword parameters: {kwargs if kwargs else 'none'}"
        return_val = f"return: {result}"

        logger.log(logging.INFO, func_name)
        logger.log(logging.INFO, pos_args)
        logger.log(logging.INFO, kw_args)
        logger.log(logging.INFO, return_val)
        logger.log(logging.INFO, "-" * 40)

        return result
    return wrapper

# Decorated functions
@logger_decorator
def greet():
    print("Hello, World!")

@logger_decorator
def check_args(*args):
    return True

@logger_decorator
def return_logger(**kwargs):
    return logger_decorator

# Main
if __name__ == "__main__":
    greet()
    check_args(1, 2, 3, "banana")
    return_logger(name="Adryan", mood="tired", debugging=True)

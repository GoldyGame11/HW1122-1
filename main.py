import logging

print('Lesson 8: Logging, Test')

logging.basicConfig(level=logging.INFO,
                    filename='logs.txt', filemode='w',
                    format='%(asctime)s:%(levelname)s:%(message)s')

def umnozhit(a:int, b:int):
    return a * b

def delit(a: int, b: int):
    return a / b

def plus(a: int, b: int):
    return a + b

def minus(a: int, b: int):
    return a - b


def perform_operation(operation, a: int, b: int):
    try:
        logging.info(f'Starting operation: {operation.__name__} with values {a} and {b}')
        result = operation(a, b)
        logging.info(f'Result of {operation.__name__}: {result}')
        return result
    except Exception as error:
        logging.error(f'Error occurred: {error}')
        return None
    finally:
        logging.info('Operation ended.')

a, b = 10, 5

add_result = perform_operation(plus, a, b)
sub_result = perform_operation(minus, a, b)
mul_result = perform_operation(umnozhit, a, b)
div_result = perform_operation(delit, a, b)


print(f"Addition result: {add_result}")
print(f"Subtraction result: {sub_result}")
print(f"Multiplication result: {mul_result}")
print(f"Division result: {div_result}")
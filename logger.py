import logging


logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
def calculate_sum(a,b):
    logger.debug(f"Calculating sum of {a} and {b}")
    result = a + b 

    logger.info(f"Sum of calculated value is: {result}")
    return result

if __name__ == '__main__':
    logger.info("starting the program")
    result = calculate_sum(10,20)
    logger.info("Program completed")
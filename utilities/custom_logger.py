import logging
import inspect
import datetime


def custom_logger(log_level=logging.DEBUG):
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    current_time = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y_%H-%M-%S')
    file_name = '../Logs/log_{}.log'.format(current_time)
    file_handler = logging.FileHandler(file_name, mode='a')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s :: %(message)s',
                                  '%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

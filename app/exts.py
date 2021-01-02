import logging
from app import app


def logger_init():
    handler = logging.FileHandler('all.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    app.logger.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    info_handler = logging.FileHandler('info.log')
    info_filter = logging.Filter()
    info_filter.filter = lambda record: record.levelno < logging.WARNING
    info_handler.setFormatter(formatter)
    info_handler.addFilter(info_filter)
    app.logger.addHandler(info_handler)

    warning_handler = logging.FileHandler('warning.log')
    warning_filter = logging.Filter()
    warning_filter.filter = lambda record:  record.levelno == logging.WARNING
    warning_handler.setFormatter(formatter)
    warning_handler.addFilter(warning_filter)
    app.logger.addHandler(warning_handler)

    error_handler = logging.FileHandler('error.log')
    error_filter = logging.Filter()
    error_filter.filter = lambda record: record.levelno == logging.ERROR
    error_handler.setFormatter(formatter)
    error_handler.addFilter(error_filter)
    app.logger.addHandler(error_handler)
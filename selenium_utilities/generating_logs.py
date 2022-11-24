import logging


def log():
    logging.basicConfig(filename="..\\Logs\\logfile.log",
                        format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    logger = logging.getLogger()
    return logger


logger = log()
logger.info('This is a new dog')
logger.info('This is an error message')
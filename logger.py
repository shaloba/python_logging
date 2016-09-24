__author__ = 'shaloba'
import logging
import time
import os
from logging.handlers import RotatingFileHandler
log_file = "test.log"
file_path = os.getcwd() + '\\logs'


if not os.path.isdir(file_path):
    os.mkdir(file_path)
logging.Formatter.converter = time.gmtime
logger = logging.getLogger()
logger.setLevel(logging.INFO)
format_handler = logging.Formatter('%(asctime)s %(threadName)-10s %(name)s %(levelname)-8s %(message)s')
handler = RotatingFileHandler(file_path + '\\' + log_file, maxBytes=2500,
                              backupCount=5)
handler.setFormatter(format_handler)
logger.addHandler(handler)


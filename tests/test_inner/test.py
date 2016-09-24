__author__ = 'shaloba'
import logging
logger = logging.getLogger(__name__)
for i in range(10):
    logger.error("This is test log line from innter test %s" % i)
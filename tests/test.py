__author__ = 'shaloba'
from test_inner import test
import logging
logger = logging.getLogger("test." + __name__)
for i in range(10):
    logger.info("This is test log line from tests\\test %s" % i)
from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

try:
    x = 1/0
except Exception as e:
    raise USvisaException(e, sys.exc_info())

'''logging.info("welcome to our Custom log")'''

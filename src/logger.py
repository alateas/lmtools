import logging
import os.path as p

log_path = p.realpath(p.join(p.dirname(p.realpath(__file__)), '../logs/'))

def log(name, message, level = logging.INFO):
    logging.basicConfig(format = u'[%(asctime)s]%(levelname)-8s|%(message)s', level = logging.INFO, filename=p.join(log_path, name+'.log'))
    logging.log(level, message)

def log_exception(name, exception):
    logging.basicConfig(format = u'[%(asctime)s]%(levelname)-8s|%(message)s', level = logging.INFO, filename=p.join(log_path, name+'.log'))
    logging.exception(exception)
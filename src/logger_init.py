import logging
import os.path as p
import settings

log_path = p.realpath(p.join(p.dirname(p.realpath(__file__)), '../logs/'))
log_level = logging.DEBUG if settings.debug else logging.INFO

def create_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    formatter=logging.Formatter('[%(asctime)s]%(levelname)-8s|%(message)s')

    handler=logging.FileHandler(p.join(log_path, name+'.log'))
    handler.setFormatter(formatter)
    handler.setLevel(log_level)

    logger.addHandler(handler)

create_logger('dhcp_manager')
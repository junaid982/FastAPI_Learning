

import os

import logging
from logging.handlers import RotatingFileHandler


def setup_logger(file_name):
    
    # 1 - Create Log Directory
    
    dir_name = "Logs"
    os.makedirs(dir_name , exist_ok=True)
    
    log_file = os.path.join(dir_name , file_name)
    
    
    # 2 - Create formatter
    formatter = logging.Formatter(
        fmt="{asctime} - {name} - {levelname} - {filename} - {funcName} : {lineno} - {message}",
        style="{"
    )
    
    # 3 - Create Handler 
    stream_handler = logging.StreamHandler()  # loggin for Cli
    rotate_file_handler = RotatingFileHandler(
        log_file,
        maxBytes=1024*1024*10,  # 10 mb file
        backupCount=3
    )
    
    
    # 4 - Configure Formatter
    stream_handler.setFormatter(formatter)
    rotate_file_handler.setFormatter(formatter)
    
    # 5 - Create Logger
    logger = logging.getLogger("Routing_project")
    logger.setLevel(logging.DEBUG)  # Setting Logger
    
    # Configure Logger
    
    logger.addHandler(stream_handler)
    logger.addHandler(rotate_file_handler)
    
    return logger
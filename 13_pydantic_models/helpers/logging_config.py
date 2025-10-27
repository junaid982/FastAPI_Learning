

import logging
from logging.handlers import RotatingFileHandler
import os


def setup_logger(file_name):
    
    # 1 - Create Loge Directory
    log_dir = "Logs"
    os.makedirs(log_dir ,exist_ok=True)
    
    log_file = os.path.join(log_dir , file_name)
    
    
    # 2 - Create Formatter
    formatter  =logging.Formatter(
        fmt="{asctime} - {name} - {levelname} - {filename} - {funcName} : {lineno} - {message}",
        style="{"
    )
    
    # 3 - Create Handler
    stream_handler = logging.StreamHandler()
    rotate_file_handler = RotatingFileHandler(
        log_file,
        maxBytes=1024*1024*10,
        backupCount=3
    )
    
    # 4 - Congigure Formatter
    stream_handler.setFormatter(formatter)
    rotate_file_handler.setFormatter(formatter)
    
    # 5 - Create Logger
    logger = logging.getLogger("Pydantic")
    
    # 6 - Configure logger
    logger.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler) 
    logger.addHandler(rotate_file_handler)
    
    return logger 
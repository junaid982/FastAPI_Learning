
import logging
from logging.handlers import RotatingFileHandler
import os


def setup_logger(file_name):
    # 1 - create Logs Diretory
    
    log_dir = "Logs"
    os.makedirs(log_dir , exist_ok=True)
    
    log_file = os.path.join(log_dir , file_name)
    
    
    # 2 - Create Formatter
    formatter = logging.Formatter(
        fmt="{asctime} - {name} - {levelname} - {filename} - {funcName} : {lineno} - {message}",
        style="{"
    ) 
    
    # 3 - Create Handler
    stream_handler = logging.StreamHandler()
    roatate_file_handler = RotatingFileHandler(
        log_file,
        maxBytes=1024*1024*10,
        backupCount=3
    )
    
    # 4 - Configure Formatter
    stream_handler.setFormatter(formatter)
    roatate_file_handler.setFormatter(formatter)
    
    
    # 5 - Create Logger
    logger = logging.getLogger("Auth Project")
    
    
    # 6 - Configure Logger
    logger.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)
    logger.addHandler(roatate_file_handler)
    
    return logger
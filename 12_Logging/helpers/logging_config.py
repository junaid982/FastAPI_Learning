

import logging
from logging.handlers import RotatingFileHandler
import os


def setup_logger():
    
    # 1 - Create Logging Directory 
    log_dir = os.path.join( "Logs")
    os.makedirs(log_dir , exist_ok=True)
    
    log_file = os.path.join(log_dir , "main.log")
    
    
    
    
    # 2 - Create handler
    stream_handler = logging.StreamHandler()   # Show logs in Terminal 
    rotate_file_handler = RotatingFileHandler(
        log_file,
        maxBytes=1024*1024*2,   # Store only two MB file 
        backupCount=3

        )   # Store logs in file 
    
    # 3 - Create formatting 
    formatter = logging.Formatter(
        fmt= "{asctime} - {name} - {levelname} - {filename} : {funcName} {lineno} - {message}",
        style="{"
    )
    
    
    # 4 - Configure Formatter
    stream_handler.setFormatter(formatter)
    rotate_file_handler.setFormatter(formatter)
    
    
    # 5 - Setup Logger
    logger = logging.getLogger("APi_to_show_logs")
    logger.setLevel(logging.DEBUG)
    # logger.addHandlers = []
    
    # Configure Handler
    logger.addHandler(stream_handler)
    logger.addHandler(rotate_file_handler)
    
    
    
    return logger
    
logger = setup_logger()
    
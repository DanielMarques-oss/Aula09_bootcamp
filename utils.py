from functools import wraps
from loguru import logger

def log_decorator(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        logger.info(f"Na função {func.__name__} nós temos os argumentos: {args}")
        try:
            result = func(*args, **kwargs)
            return result
        
        except:
            logger.critical("Digite valores corretos")
    
    return wrapped
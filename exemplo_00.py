from loguru import logger
from utils import log_decorator
import sys

#logger.add("file_{time}.log", level="CRITICAL")

@log_decorator
def soma(x, y):
    return x + y

soma(3, 4)
soma(5, 2)
soma(2, "1")

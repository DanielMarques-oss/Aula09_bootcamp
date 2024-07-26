from loguru import logger
import sys

logger.add("file_{time}.log", level="CRITICAL")


def soma(x, y):
    try:
        logger.info(x)
        logger.warning(y)
        logger.info(x + y)

    except:
        logger.critical("Favor digitar números para ambas as entradas")

soma(3, 4)
soma(1, 2)
soma(2, "1")

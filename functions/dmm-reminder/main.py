import logging

from flask import Request

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.propagate = False


def remind_dmm(request: Request):
    logger.info(request.args)
    logger.info(request)
    logger.info(request)
    return 'Hello!!!!!'

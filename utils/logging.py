import logging

logger: logging.Logger


def init():
    global logger

    logger = logging.getLogger("weather-app")
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter("%(asctime)-15s  %(levelname)s   %(message)s"))
    logger.addHandler(ch)

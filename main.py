import schedule
import time
from configs import config
from db import mongo
from service import openweather
from utils import logging
from dao import weatherdao


if __name__ == '__main__':

    config.init()
    logging.init()
    mongo.init()
    openweather.init()

    weatherdao.init()

    schedule.every().minute.at(":20").do(openweather.get_and_save)

    logging.logger.info("Successfully Started")
    logging.logger.info(f"target mongo host: {config.get_string('mongodb', 'uri')}")

    config.reset()

    while 1:
        schedule.run_pending()
        time.sleep(1)

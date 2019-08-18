import pymongo
from pymongo import database
from configs import config
from utils import logging

client: pymongo.MongoClient
db: database.Database


def init():
    global client, db
    client = pymongo.MongoClient(config.get_string("mongodb", "uri"))
    db_name = config.get_string("mongodb", "db")
    db = client[db_name]

    while 1:
        logging.logger.info(f"locating db {db_name}")
        dbs = client.list_database_names()
        if db_name in dbs:
            logging.logger.info(f"located db {db_name}")
            break




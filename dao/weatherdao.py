from pymongo.collection import Collection
from db import mongo
from models.weather import WeatherRecord
from utils import logging

collection: Collection


def init():
    global collection
    collection = mongo.db["weather"]
    logging.logger.info(f"located collection weather")


def save(record: WeatherRecord):
    logging.logger.info(f"saving weather record for {record.location}")
    collection.insert_one(record.to_dict())

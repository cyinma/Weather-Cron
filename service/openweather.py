import requests
import datetime
from configs import config
from utils import logging
from models.weather import OpenWeatherRes, Location
from dao import weatherdao


api_key: str
api_url = "http://api.openweathermap.org/data/2.5/weather"
open_weather_dict = {
    "HK": 1819730,
    "SG": 1880252
}


def init():
    global api_key
    api_key = config.get_string("openWeather", "key")


def get_current_weather(location: str):
    logging.logger.info(f"getting weather data of {location}")
    if location not in open_weather_dict:
        return None

    res = requests.get(f"{api_url}?id={open_weather_dict[location]}&APPID={api_key}")
    data = OpenWeatherRes.from_json(res.content)
    return data.main


def get_and_save():
    # timestamp in :30 of current minute
    ts = int(datetime.datetime.now().replace(second=30, microsecond=0).timestamp())
    hk = get_current_weather("HK").to_record(Location.HK.name, ts)
    sg = get_current_weather("SG").to_record(Location.SG.name, ts)

    if not (hk is None):
        weatherdao.save(hk)

    if not (sg is None):
        weatherdao.save(sg)

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from enum import Enum


@dataclass
@dataclass_json
class OpenWeather:
    temp: float
    pressure: int
    humidity: float
    temp_min: float
    temp_max: float

    def to_record(self, location: str, ts: int):
        return WeatherRecord(
            location=location,
            timestamp=ts,
            temp=round(self.temp - 273.15, 2),
            pressure=self.pressure,
            humidity=round(self.humidity, 2),
            temp_min=round(self.temp_min - 273.15, 2),
            temp_max=round(self.temp_max - 273.15, 2)
        )


@dataclass
@dataclass_json
class OpenWeatherRes:
    main: OpenWeather


@dataclass
@dataclass_json
class Location(Enum):
    HK = "HK",
    SG = "SG"


@dataclass
@dataclass_json
class WeatherRecord:
    location: str
    timestamp: int
    temp: float
    pressure: int
    humidity: float
    temp_min: float
    temp_max: float

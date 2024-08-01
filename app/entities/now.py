from dataclasses import dataclass
from datetime import datetime


@dataclass
class Now():
    '''
    Температура сейчас
    '''
    
    temperature_2m: int = None
    # Относительная влажность
    relative_humidity_2m: int = None
    # Ощутимая температура
    apparent_temperature: int = None
    # Дождь
    rain: bool = None
    # Снег
    snowfall: bool = None
    # Поверхностное давление
    surface_pressure: int = None
    # Скорость ветра
    wind_speed_10m: int = None
    # Время
    time: datetime = None
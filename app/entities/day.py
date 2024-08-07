from dataclasses import dataclass
from datetime import datetime


@dataclass
class Day():
    '''
    Температура на день 
    '''
    # Температура
    temperature_2m_max: float = None
    # Вероятность осадков
    precipitation_probability_max: int = None
    # Максимальная скорость ветра
    wind_speed_10m_max: float = None
    # Время
    time: datetime = None
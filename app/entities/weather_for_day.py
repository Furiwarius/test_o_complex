from dataclasses import dataclass
from datetime import datetime


@dataclass
class WeatherForDay():
    '''
    Погода на день
    '''
    
    # Время
    times: list
    # Температура
    temperatures: list
    # Вероятность осадков
    precipitation_probability:list
    # скорость ветра
    wind_speed:list
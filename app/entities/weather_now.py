from dataclasses import dataclass
from datetime import datetime


@dataclass
class WeatherNow():
    '''
    Погода сейчас
    '''
    
    # Время
    time: datetime
    # Температура
    temperature: float
    # Температура по ощущениям
    apparent_temperature: float
    # Вероятность осадков
    precipitation_probability:float
    # Давление
    surface_pressure:float 
    # скорость ветра
    wind_speed:float
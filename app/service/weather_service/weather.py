
from app.service.geolocator.geolocator import Geolocator
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry


class WeatherSearchEngine():
    '''
    Поисковик погоды
    '''


    def __init__(self) -> None:
        
        self.lokator = Geolocator()



    def _setting(self) -> None:
        '''
        Настройка параметров
        '''
        url = "https://api.open-meteo.com/v1/forecast"

        cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
        retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
        openmeteo = openmeteo_requests.Client(session = retry_session)

        coordinates=self.lokator.get_coordinates()

        # Параметры для запроса
        params = {
            # Широта
            "latitude": coordinates[0],
            # Долгота
            "longitude": coordinates[1],
            # Ежечасно
            "hourly": ["temperature_2m", "relative_humidity_2m", "apparent_temperature",
                    "precipitation_probability", "precipitation", "rain", "snowfall",
                    "surface_pressure", "cloud_cover", "cloud_cover_mid", "wind_speed_10m"],
            # Ежедневно 
            "daily": ["temperature_2m_max", "apparent_temperature_max", "precipitation_hours", 
                "precipitation_probability_max", "wind_speed_10m_max"],
            # Часовой пояс
            "timezone": 'auto'}

        # Запрос данных по параметрам
        self.responses = openmeteo.weather_api(url, params=params)[0]

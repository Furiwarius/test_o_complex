from app.service.geolocator.geolocator import Geolocator
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
from datetime import datetime, timezone, timedelta
from app.utils.round_time import round_time
from app.settings import weather_settings



class WeatherSearch():
    '''
    Поисковик погоды
    '''


    def __init__(self) -> None:
        
        self.locator = Geolocator()
        self._setting_service()


    def _setting_service(self) -> None:
        '''
        Настройка сервиса
        '''
        self.url = "https://api.open-meteo.com/v1/forecast"

        cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
        retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
        self.openmeteo = openmeteo_requests.Client(session = retry_session)


    def _setting_parameters(self, location:str) -> None:
        '''
        Настройка параметров для поиска
        '''

        # Получаем координаты локации
        coordinates=self.locator.get_coordinates(location)

        # Параметры для запроса
        self.params = {
            # Широта
            "latitude": coordinates[0],
            # Долгота
            "longitude": coordinates[1],
            # Ежечасно
            "current": weather_settings.current_params,
            # Ежедневно 
            "daily": weather_settings.daily_params,
            # Часовой пояс
            "timezone": 'GMT',
            # Количество дней для отслеживания
            "forecast_days": weather_settings.amount_days}
    


    def get_weather(self, location:str) -> dict:
        '''
        Получить погоду по городу
        '''
        self._setting_parameters(location)
        # Запрос данных по параметрам
        self.response = self.openmeteo.weather_api(self.url, params=self.params)[0]
        self._current_data_generation()
        self._daily_data_generation()

        return {"current":self.current_data, "daily":self.daily_data}



    def _current_data_generation(self) -> None:
        '''
        Формирование данных на текущее время
        '''

        current = self.response.Current()

        datas = [current.Variables(index).ValuesAsNumpy() for index, _ in enumerate(self.params["current"])]
        
        self.current_data = {param:datas for datas, param in zip(datas, self.params["current"])}
        self.current_data["time"] = current.Time()
        



    def _daily_data_generation(self) -> None:
        '''
        Формирование данных для дней
        '''
        # Формирование данных по дням
        daily = self.response.Daily()
        datas = [daily.Variables(index).ValuesAsNumpy() for index, _ in enumerate(self.params["daily"])]
        
        self.daily_data = {param:datas for datas, param in zip(datas, self.params["daily"])}
        self.daily_data["time"]
        
    
    
from app.service.geolocator.geolocator import Geolocator
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
from datetime import datetime, timezone, timedelta
from app.utils.round_time import round_time

hourly_params = ["temperature_2m", "precipitation",
                    "surface_pressure", "wind_speed_10m"]

daily_params = ["temperature_2m_max", "precipitation_hours", "wind_speed_10m_max"]


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
            "hourly": hourly_params,
            # Ежедневно 
            "daily": daily_params,
            # Часовой пояс
            "timezone": 'GMT',
            # Количество дней для отслеживания
            "forecast_days": 3}
    


    def get_weather(self, location:str) -> dict:
        '''
        Получить погоду по городу
        '''
        self._setting_parameters(location)
        # Запрос данных по параметрам
        self.response = self.openmeteo.weather_api(self.url, params=self.params)[0]
        self._hourly_data_generation()
        self._daily_data_generation()

        return {"hourly":self.hourly_dataframe.loc[str(round_time(datetime.now(timezone.utc)))], 
                "daily":self.daily_dataframe}



    def _hourly_data_generation(self) -> None:
        '''
        Формирование данных по часам
        '''
        # Формирование почасовых данных
        hourly = self.response.Hourly()
        # Почасовая температура 2 мм
        nympy_datas = [hourly.Variables(index).ValuesAsNumpy() for index, _ in enumerate(self.params["hourly"])]
        
        data_dict = {param:datas for datas, param in zip(nympy_datas, self.params["hourly"])}
        self.hourly_dataframe = pd.DataFrame(data = data_dict)
        self.hourly_dataframe.index = pd.date_range(
            start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
            end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
            freq = pd.Timedelta(seconds = hourly.Interval()),
            inclusive = "left"
            )
        self.hourly_dataframe.index.name = "date"
        



    def _daily_data_generation(self) -> None:
        '''
        Формирование данных для дней
        '''
        # Формирование данных по дням
        daily = self.response.Daily()
        # Почасовая температура 2 мм
        nympy_datas = [daily.Variables(index).ValuesAsNumpy() for index, _ in enumerate(self.params["daily"])]
        
        data_dict = {param:datas for datas, param in zip(nympy_datas, self.params["hourly"])}
        self.daily_dataframe = pd.DataFrame(data = data_dict)
        self.daily_dataframe.index = pd.date_range(
            start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
            end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
            freq = pd.Timedelta(seconds = daily.Interval()),
            inclusive = "left"
            )
        self.daily_dataframe.index.name = "date"
        
    
    
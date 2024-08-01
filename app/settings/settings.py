

class WeatherSettings():
    '''
    Настройки для api погоды
    '''
    # Запрашиваемые параметры для часов
    hourly_params = ["temperature_2m", "precipitation",
                    "surface_pressure", "wind_speed_10m"]
    # Запрашиваемые параметры для дней
    daily_params = ["temperature_2m_max", "precipitation_hours", "wind_speed_10m_max"]
    # Количество дней для отслеживания
    amount_days = 3


class DatabaseSettings():
    '''
    Настройки для базы данных
    '''

    # Строка подключения БД
    name = f"sqlite:///app/database/weather.db"
    # Автообновление данных
    autoflush=False
    # Автоматическое логгирование БД
    echo=False

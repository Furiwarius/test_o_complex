import os
import dotenv

dotenv.load_dotenv()


class WeatherSettings():
    '''
    Настройки для api погоды
    '''
    # Запрашиваемые параметры для часов
    current_params = ["temperature_2m", "relative_humidity_2m", "apparent_temperature",
                      "rain", "snowfall", "surface_pressure", "wind_speed_10m"]
    # Запрашиваемые параметры для дней
    daily_params = ["temperature_2m_max", "precipitation_probability_max", "wind_speed_10m_max"]
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


class AdminServiceSetting():
    '''
    Настройки для администраторской бизнес-логики
    '''
    # Секретный ключ, добавляемый в администраторские ключи при хешировании
    secret = os.getenv("SECRET")

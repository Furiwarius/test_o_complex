from app.settings.settings import DatabaseSettings, WeatherSettings, AdminServiceSetting
from functools import lru_cache


db_settings = DatabaseSettings()
weather_settings = WeatherSettings()

@lru_cache
def get_admin_settings():
    return AdminServiceSetting()
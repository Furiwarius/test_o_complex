from datetime import datetime, timezone


def message_render(data:dict, location: str) -> str:
    '''
    Формирование сообщения из словаря с данныи
    полученныйми от weather_service
    '''
    now = datetime.now(timezone.utc)
    hourly = data.get("hourly")
    weather_now = f'''Сейчас {now.hour}:{now.minute}
        Погода в городе {location}е
        сегодня: температура {round(hourly["temperature_2m"])} С,
        скорость ветра {round(hourly["wind_speed_10m"])} м/ч,
        осадки {hourly["precipitation"]} мм,
        давление {round(hourly["surface_pressure"])}'''


    return weather_now
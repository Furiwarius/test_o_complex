from geopy.geocoders import Nominatim
from app.errors.service_errors import InvalidLocation


class Geolocator():
    '''
    Класс для поиска координат по названию города
    '''

    def __init__(self) -> None:
        
        self.lokator = Nominatim(user_agent="MyApp")
    

    def get_coordinates(self, city:str) -> tuple:
        '''
        Получить координаты по названию города
        '''

        location = self.lokator.geocode(city)
        if location is None:
            raise InvalidLocation(f"The geolocator could not find the coordinates of this place (city : {city})")
        
        return (location.latitude, location.longitude)
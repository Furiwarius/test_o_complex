from geopy.geocoders import Nominatim
from app.errors.service_errors import InvalidLocation


class Geolocator():
    '''
    Класс для поиска координат по названию города
    '''

    def __init__(self) -> None:
        
        self.lokator = Nominatim(user_agent="MyApp")
    

    def get_coordinates(self, sity:str) -> tuple:
        '''
        Получить координаты по названию города
        '''

        location = self.lokator.geocode(sity)
        if location is None:
            raise InvalidLocation("The geolocator could not find the coordinates of this place")
        
        return (location.latitude, location.longitude)
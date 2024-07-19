from geopy.geocoders import Nominatim

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

        return (location.latitude, location.longitude)
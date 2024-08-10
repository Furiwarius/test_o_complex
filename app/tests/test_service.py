from app.service.geolocator.geolocator import Geolocator
from faker import Faker
from random import randrange
import pytest
from app.errors.service_errors import InvalidLocation


class TestService():
    '''
    Класс для тестирования бизнес-логики
    '''


    def test_get_coordinates(self, 
                             fake = Faker(locale="ru"),
                             coordinate = Geolocator()):
        '''
        Тестирование метода по получению координат
        по названию места
        '''

        valid_locations = [fake.city_name() for _ in range(10)]
        invalid_locations = [city+str(randrange(10)) for city in valid_locations]

        for location in valid_locations:
            coordinate.get_coordinates(location)

        with pytest.raises(InvalidLocation):
            for location in invalid_locations:
                coordinate.get_coordinates(location)
from random import randrange
import pytest
from app.errors.service_errors import InvalidLocation


class TestService():
    '''
    Класс для тестирования бизнес-логики
    '''


    def test_get_coordinates(self, fake, coordinate):
        '''
        Тестирование метода по получению координат
        по названию места
        '''

        valid_locations = fake.city_name()
        invalid_locations = valid_locations+str(randrange(10))

        coordinate.get_coordinates(valid_locations)

        with pytest.raises(InvalidLocation):
            coordinate.get_coordinates(invalid_locations)
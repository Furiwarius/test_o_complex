from app import app
from fastapi import status
import pytest
from fastapi.testclient import TestClient
from app.service.admin_service import AdminService
from faker import Faker


class TestAdminApi():
    '''
    Класс для тестирования api админа
    '''

    client = TestClient(app)
    key = AdminService().new_key()
    fake = Faker(locale="ru")



    @pytest.mark.asyncio
    async def test_get_count_user(self):
        '''
        Тестирование метода по получению количества пользователей
        '''
        response = self.client.post("/get_count_user",
                                    json={"admin_key": self.key})
        
        assert response.status_code == status.HTTP_200_OK
        
        answer = response.json()
        assert answer["answer"]
    


    @pytest.mark.asyncio
    async def test_get_count_request(self):
        '''
        Тестирование метода по получению количества 
        обращений для получения погоды по данной локации
        '''
        location = self.fake.city_name()

        # Отправляем запрос на получение погоды
        response = self.client.post("/weather",
                                    json={"sity":location},
                                    cookies={"user_id":"1"})
        assert response.status_code == status.HTTP_200_OK

        # После чего просим количество запросов по данной локации
        response = self.client.post("/get_count_reauest",
                                    json={"key":{"admin_key": self.key}, 
                                          "location":{"sity":location}})
        
        assert response.status_code == status.HTTP_200_OK
        
        answer = response.json()
        assert answer["answer"]
    


    @pytest.mark.asyncio
    async def test_get_max_count_request(self):
        '''
        Тестирование метода по получению локации с максимальным количеством запросов

        '''
        response = self.client.post("/get_max_count_reauest",
                                    json={"admin_key": self.key})
        
        assert response.status_code == status.HTTP_200_OK
        
        answer = response.json()
        assert answer["answer"]
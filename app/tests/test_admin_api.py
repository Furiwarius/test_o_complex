from fastapi import status
import pytest


class TestAdminApi():
    '''
    Класс для тестирования api админа
    '''


    @pytest.mark.asyncio
    async def test_get_count_user(self, async_client, admin_key):
        '''
        Тестирование метода по получению количества пользователей
        '''
        response = await async_client.post("/get_count_user",
                                    json={"admin_key": admin_key})
        
        assert response.status_code == status.HTTP_200_OK
    


    @pytest.mark.asyncio
    async def test_get_count_request(self, async_client, admin_key, fake):
        '''
        Тестирование метода по получению количества 
        обращений для получения погоды по данной локации
        '''
        location = fake.city_name()

        # Отправляем запрос на получение погоды
        response = await async_client.post("/weather",
                                    json={"sity":location},
                                    cookies={"user_id":"1"})
        assert response.status_code == status.HTTP_200_OK

        # После чего просим количество запросов по данной локации
        response = await async_client.post("/get_count_reauest",
                                    json={"key":{"admin_key": admin_key}, 
                                          "location":{"sity":location}})
        
        assert response.status_code == status.HTTP_200_OK
    


    @pytest.mark.asyncio
    async def test_get_max_count_request(self, async_client, admin_key):
        '''
        Тестирование метода по получению локации с максимальным количеством запросов

        '''
        response = await async_client.post("/get_max_count_reauest",
                                    json={"admin_key": admin_key})
        
        assert response.status_code == status.HTTP_200_OK
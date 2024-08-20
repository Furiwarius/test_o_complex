from fastapi import status
import pytest



class TestApi():
    '''
    Класс для тестирования api
    '''
    
    @pytest.mark.asyncio
    async def test_cookie(self, async_client):
        '''
        Тестирование методы по установке cookie
        '''

        response = await async_client.get("/cookie")
        assert response.status_code == status.HTTP_200_OK
    


    @pytest.mark.asyncio
    async def test_index_page(self, async_client):
        '''
        Тестирование получения индесной страницы
        '''
        response = await async_client.get("/")
        assert response.status_code == status.HTTP_200_OK
    


    @pytest.mark.asyncio
    async def test_weather(self, async_client):
        '''
        Тестирование метода по получению данных о погоде
        '''
        response = await async_client.post("/weather",
                                    json={"sity":"Kaliningrad"},
                                    cookies={"user_id":"1"})
        
        assert response.status_code == status.HTTP_200_OK

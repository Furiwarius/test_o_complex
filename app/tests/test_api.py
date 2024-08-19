from app import app
from fastapi import status
import pytest
from fastapi.testclient import TestClient



class TestApi():
    '''
    Класс для тестирования api
    '''
    client = TestClient(app)


    @pytest.mark.asyncio
    async def test_cookie(self):
        '''
        Тестирование методы по установке cookie
        '''
        response = self.client.get("/cookie")
        assert response.status_code == status.HTTP_200_OK
        
        answer = response.json()
        assert answer["message"] == "куки установлены"



    @pytest.mark.asyncio
    async def test_index_page(self):
        '''
        Тестирование получения индесной страницы
        '''
        response = self.client.get("/")
        assert response.status_code == status.HTTP_200_OK
    


    @pytest.mark.asyncio
    async def test_weather(self):
        '''
        Тестирование метода по получению данных о погоде
        '''
        response = self.client.post("/weather",
                                    json={"sity":"Kaliningrad"},
                                    cookies={"user_id":"1"})
        
        assert response.status_code == status.HTTP_200_OK
        
        answer = response.json()
        assert answer["message"]["current"] and answer["message"]["daily"]

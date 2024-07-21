from fastapi import FastAPI
from app.api.routes import router



class Application():
    '''
    Приложение
    '''

    def create_app(self) -> FastAPI:
        '''
        Создание приложения
        '''
        self.app = FastAPI()
        self.app.include_router(router)

        return self.app

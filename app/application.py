from fastapi import FastAPI
from app.api.routes import router
from fastapi.staticfiles import StaticFiles


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
        
        self.app.mount("/static", StaticFiles(directory="app/static"))
        
        return self.app

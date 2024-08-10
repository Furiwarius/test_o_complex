from app.errors.base_exception import BaseException


class InvalidLocation(BaseException):
    '''
    Вызывается, если геолокатор не смог 
    найти координаты по переданному месту
    '''
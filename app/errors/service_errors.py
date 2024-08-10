from app.errors.base_exception import BaseException


class InvalidLocation(BaseException):
    '''
    Вызывается, если геолокатор не смог 
    найти координаты по переданному месту
    '''

class SecretNotFound(BaseException):
    '''
    Вызывается, если в файле окружения
    отстутствует переменная SECRET, добавляемая
    в администраторский ключ
    '''
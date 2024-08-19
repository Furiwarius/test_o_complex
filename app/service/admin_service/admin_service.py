from datetime import datetime, timezone
from app.utils.to_hash import to_hash
from app.database.admin_cruds import AdminCRUD
from app.settings import get_admin_settings
from app.errors.service_errors import SecretNotFound, InvalidKey


class AdminService():
    '''
    Класс для проверки ключа админа 
    и генерации нового
    '''

    admin_crud = AdminCRUD()
    setting = get_admin_settings()


    def new_key(self) -> str:
        '''
        Генерация нового ключа администратора
        '''
        if self.setting.secret is None:
            raise SecretNotFound("The Secret variable is missing from the environment files")
        
        last_id = self.admin_crud.get_last_one()
        if last_id is None:
            new_id = 1
        else: 
            new_id = last_id+1
        
        new_key = to_hash(f"{new_id}{datetime.now(timezone.utc)}{self.setting.secret}")
        self.admin_crud.add_admin(key=new_key)

        return new_key


    def key_verification(self, key:str) -> None:
        '''
        Проверка ключа
        '''
        if not self.admin_crud.check_exist(key=key):
            raise InvalidKey("Incorrect key passed")
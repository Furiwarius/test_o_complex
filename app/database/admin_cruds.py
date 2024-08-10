from app.database.database import Database
from app.database.tables.essence import HistoryTable, User, Admin


class AdminCRUD():
    '''
    Класс для сбора данных из БД
    '''

    def add_admin(self, key:str) -> str:
        '''
        Получает хешированный ключ админа и добавляет его в бд
        '''

        with Database() as db:
            new_admin = Admin(admin_key=key)
            db.add(new_admin)
            db.commit()

            return new_admin.admin_key
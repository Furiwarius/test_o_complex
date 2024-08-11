from app.database.database import Database
from app.database.tables.essence import HistoryTable, User, Admin
from sqlalchemy import func


class AdminCRUD():
    '''
    Класс для сбора данных из БД
    '''


    def check_exist(self, key:str) -> bool:
        '''
        Проверка наличия ключа
        '''
        with Database() as db:
            result = db.query(Admin.id).filter(Admin.admin_key==key).scalar()
        
        if result: 
            return True
        return False



    def add_admin(self, key:str) -> str:
        '''
        Получает хешированный ключ админа и добавляет его в бд
        '''

        with Database() as db:
            new_admin = Admin(admin_key=key)
            db.add(new_admin)
            db.commit()

            return new_admin.admin_key
    


    def get_last_one(self) -> int|None:
        '''
        Получить последний id добавленный в таблицу admin
        '''
        with Database() as db:
            result = db.query(Admin.id).order_by(Admin.id.desc()).first()
        if result:
            return result[0]
        
    

    def get_count_user(self) -> int:
        '''
        Получить количество пользователей
        '''
        with Database() as db:
            result = db.query(func.count(User.id)).scalar()
        
        return result
    
    

    def get_count_request(self, location:str) -> int:
        '''
        Получить количество запросов по данной локации
        '''
        with Database() as db:
            result = db.query(HistoryTable.count).filter(HistoryTable.sity==location).scalar()
        
        return result



    def get_max_count_request(self) -> str|None:
        '''
        Получить локацию с максимальным
        количеством запросов
        '''

        with Database() as db:
            max_count = db.query(func.max(HistoryTable.count)).scalar()
            result = db.query(HistoryTable.sity).filter(HistoryTable.count==max_count).scalar()
            
        return result

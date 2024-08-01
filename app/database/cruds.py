from app.database.database import Database
from datetime import datetime, timezone
from app.database.tables.essence import HistoryTable, User


class ApplicationCRUD():
    '''
    Класс для добавления пользователей и записей в БД
    '''
    
    
    def add_user(self) -> int:
        '''
        Добавить пользователя и вернуть его id
        '''
        with Database() as db:
            user = User()
            db.add(user)
            db.commit()

            return user.id



    def add_record(self, request:str, user_id:int) -> None:
        '''
        Добавить запись в таблицу с историей поиска
        '''
        with Database() as db:
            history_id = db.query(HistoryTable.id).filter(HistoryTable.sity==request, 
                                                          HistoryTable.user_id==user_id).all()
            if len(history_id)==0 :
                new_history = HistoryTable(sity=request, user_id=user_id, count=1)
                db.add(new_history)
                db.commit()
                
            else:
                history = db.get(HistoryTable, history_id[0])
                db.query(HistoryTable).filter(HistoryTable.id == history.id).update({HistoryTable.count:history.count+1}, 
                                                        synchronize_session = False)
                db.commit()
                
            


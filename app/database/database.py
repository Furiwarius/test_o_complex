from sqlalchemy import create_engine, Engine
from app.settings import db_settings
from app.database.tables.essence import Base
from sqlalchemy.orm import Session


class Database():
    '''
    База данных

    Имеет всего 1 экземпляр на все приложение
    '''

    _instance = None  # Приватное поле для хранения единственного экземпляра



    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._new_engine()
            cls._instance._create_table()
        return cls._instance
    


    def __enter__(self) -> Session:
        self.__new__(self)
        with Session(autoflush=db_settings.autoflush, bind=self.engine) as db:
            self.session = db
            return self.session


    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self.session:
            self.session.close()



    def _new_engine(self) -> Engine:
        '''
        Создание движка SQLalchemy
        '''
        # строка подключения
        sql_database = db_settings.name
        # создаем движок SqlAlchemy
        self.engine = create_engine(sql_database, echo=db_settings.echo, connect_args={"check_same_thread": False}) 



    def _create_table(self) -> None:
        '''
        Создание таблиц
        '''
        # создаем таблицы
        Base.metadata.create_all(bind=self.engine)
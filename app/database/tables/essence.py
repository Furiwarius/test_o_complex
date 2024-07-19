from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy import Column, DateTime, Boolean
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    '''
    Базовый класс для моделей
    '''


class UserTable(Base):
    '''
    Модель таблицы user
    '''
    __tablename__ = "user"

    # токен по которому будуд отслеживаться пользователи
    name = Column(String(60), primary_key=True, unique=True)
    status = Column(Boolean, default=True, nullable=False)
    create_date = Column(DateTime, default=datetime.now, nullable=False)



class HistoryTable(Base):
    '''
    Модель таблицы history
    '''
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, 
                index=True, autoincrement='auto', unique=True)
    user_id = Column(Integer, ForeignKey("user.name"), nullable=False)
    sity = Column(String(60), nullable=False)
    create_date = Column(DateTime, default=datetime.now, nullable=False)


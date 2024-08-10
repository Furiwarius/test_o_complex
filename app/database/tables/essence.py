from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy import Column, DateTime, Boolean, func
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase



class Base(DeclarativeBase):
    '''
    Базовый класс для моделей
    '''
    id = Column(Integer, primary_key=True, 
                index=True, autoincrement='auto', unique=True)



class User(Base):
    '''
    Модель пользователя
    '''
    __tablename__ = "user"



class HistoryTable(Base):
    '''
    Модель таблицы history
    '''
    __tablename__ = "history"

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    sity = Column(String(60), nullable=False)
    count = Column(Integer, nullable=False)



class Admin(Base):
    '''
    Модель таблицы с ключами администраторов 
    '''
    __tablename__ = "admin"

    admin_key = Column(String(65), nullable=False, unique=True)
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy import Column, DateTime, Boolean, func
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    '''
    Базовый класс для моделей
    '''

class HistoryTable(Base):
    '''
    Модель таблицы history
    '''
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, 
                index=True, autoincrement='auto', unique=True)
    sity = Column(String(60), nullable=False)
    count = Column(Integer, nullable=False)


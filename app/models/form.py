from app.db.db import Base
from sqlalchemy.schema import CreateTable
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped

class OrderForm(Base): # форма принятия заказа
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(Integer, unique=True)
    address: Mapped[str] = mapped_column(String)

class Products(Base): # список продуктов
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    stock: Mapped[int] = mapped_column(Integer)

class Cart(Base): #корзина
    __tablename__ = 'cart'

    name: Mapped[str] = mapped_column(String, primary_key=True)
    amount: Mapped[int] = mapped_column(Integer)

print(CreateTable(OrderForm.__table__)) # создаем таблицы
print(CreateTable(Products.__table__))
print(CreateTable(Cart.__table__))
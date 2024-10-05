from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import insert, select
from typing import Annotated
from app.db.db_depends import get_db
from app.schemas import CreateOrder, Product
from fastapi.responses import HTMLResponse
from app.models.form import OrderForm, Products, Cart

router = APIRouter()

@router.get('/form', response_class=HTMLResponse) #роут для возвраат формы
async def create_form():
    html_content = '''...'''
    return HTMLResponse(content=html_content, status_code=status.HTTP_200_OK)

@router.get('/order/{id}') #роут для получения информации о заказе
async def get_order_info(db: Annotated[Session, Depends(get_db)], id: int):
    order = db.scalar(select(OrderForm).where(OrderForm.id == id))
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Такого заказа нет')
    return order

@router.post('/form/order') #роут для обработки формы заказа и отправки данных в бд
async def create_an_order(db: Annotated[Session, Depends(get_db)], order: CreateOrder):
    db.execute(insert(OrderForm).values(name=order.name,
                                        phone=order.number,
                                        address=order.address)) #отправляем данные принятые с формы заказа в бд
    db.commit()
    return {'status': status.HTTP_201_CREATED}

@router.get('/info') #потенциальный роут для кнопки "О нас" на сайте
async def about_us():
    pass

@router.get('/product/{id}') #роут для получения инфы о конкретном товаре на сайте
async def get_product(db: Annotated[Session, Depends(get_db)], id: int):
    product = db.scalar(select(Products).where(Products.id == id, Products.stock > 0)) #проверям на наличие в ассортименте
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Продукт не найден')
    return product

@router.post('/cart/add') #роут для добавления товаров в корзину
async def add_to_cart(db: Annotated[Session, Depends(get_db)], product: Product):
    add = db.scalars(select(Products).where(Products.stock > 0)).all() #узнаем в наличии ли продукт
    if add is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='такого продукта не существует')
    db.execute(insert(Cart).values(name=product.name, amount=product.amount)) #отправляем в бд коризны данные о добавленном продукте
    db.commit()
    return {'status': status.HTTP_201_CREATED}
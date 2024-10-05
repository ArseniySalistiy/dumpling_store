from pydantic import BaseModel
# тут пайдентик модели
class CreateOrder(BaseModel):
    id: int
    name: str
    address: str
    number: int

class Product(BaseModel):
    name: str
    amount: int
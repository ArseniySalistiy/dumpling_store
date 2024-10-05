from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

#в этом файле подлкючаем бд
engine = create_engine('sqlite:///store.db', echo=True)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
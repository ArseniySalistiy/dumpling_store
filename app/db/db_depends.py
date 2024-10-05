from app.db.db import SessionLocal
#тут мы ловим ошибки возникающие при работе с бд и после завершения работы с бд закрываем ее
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
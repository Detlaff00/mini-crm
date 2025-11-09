from fastapi import FastAPI
from .routers import clients
from .database import Base, engine
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db, Base, engine

app = FastAPI(title="Mini_crm")

@app.get("/")
def root():
    return {"message": "Welcome to Mini CRM API"}


# создаём таблицы в БД
Base.metadata.create_all(bind=engine)


app.include_router(clients.router)

@app.get("/")
def root():
    return {"message": "Mini CRM API работает!"}

@app.get("/test-db")
def test_db_connection(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "✅ Подключение к БД успешно"}
    except Exception as e:
        return {"status": "❌ Ошибка подключения", "details": str(e)}
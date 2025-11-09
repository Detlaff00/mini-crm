from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy import text
import os

# Загружаем переменные окружения
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Создаем подключение к базе
engine = create_engine(DATABASE_URL)

# Сессия для взаимодействия с БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()

# Dependency — для FastAPI
def get_db():
    db = SessionLocal()
    try:
        db.execute(text("SELECT 1"))  
        yield db
    finally:
        db.close()

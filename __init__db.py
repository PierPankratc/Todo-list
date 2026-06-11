# init_db.py
from db.models import Base
from db.create_db import engine

def init_database():
    print("Создаю таблицы в базе данных...")
    Base.metadata.create_all(bind=engine)
    print("✅ Таблицы успешно созданы!")

if __name__ == "__main__":
    init_database()
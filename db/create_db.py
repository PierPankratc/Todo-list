from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

class Base(DeclarativeBase):
    pass

# --- НАСТРОЙКА ПОДКЛЮЧЕНИЯ ---
engine = create_engine(url='sqlite:///todo.db', echo=True)

# 1. Создаём фабрику сессий (ОДИН РАЗ)
SessionLocal = sessionmaker(bind=engine)

# 2. Функция-зависимость для FastAPI (ВОЗВРАЩАЕТ СЕССИЮ)
def get_db_connect():
    db = SessionLocal()  # Создаём сессию из фабрики
    try:
        yield db         # Передаём сессию в эндпоинт
    finally:
        db.close()       # Закрываем сессию

# 3. Функция для создания таблиц
def create_db():
    Base.metadata.create_all(bind=engine)
    print("✅ База данных и таблицы созданы!")

# Создаём таблицы при запуске модуля
create_db()
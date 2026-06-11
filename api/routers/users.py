from fastapi import APIRouter, Depends
from db.create_db import get_db_connect, create_db  # create_db импортировать необязательно, он уже вызван
from api.schemas import UserSchema
from sqlalchemy.orm import Session
from db.models import Users

router = APIRouter(prefix='/user', tags=['Пользователи'])

@router.post('/login')
def login(user: UserSchema, db: Session = Depends(get_db_connect)):
    # Ищем пользователя по имени
    new_user = db.query(Users).filter(Users.name == user.name).first()
    if new_user:
        return {'Auth': True, 'user_id': new_user.id}
    else:
        # Создаём нового пользователя
        new_user = Users(name=user.name)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {'Auth': True, 'user_id': new_user.id, 'message': 'Пользователь создан'}

@router.get('/tasks/{id}')
def get_tasks(id: int, db: Session = Depends(get_db_connect)):
    user = db.query(Users).filter(Users.id == id).first()
    if not user:
        return {'User': 'Not Found'}
    # ИСПРАВЛЕНО: было user.todo, нужно user.todos
    return user.todos  # Возвращает список задач пользователя

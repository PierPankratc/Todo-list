from fastapi import APIRouter, Depends
from db.create_db import get_db_connect # create_db импортировать необязательно, он уже вызван
from api.schemas import UserSchema, TaskSchema
from sqlalchemy.orm import Session
from db.models import Users, Todo

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
    task_list = []
    for task in user.todos:
         task_list.append ({
               f'{task.id}': task.task,
               'status': task.status
         })
    return task_list
      # Возвращает список задач пользователя

@router.post('/add_task/{id}')
def add_task(id: int, task: TaskSchema, db: Session = Depends(get_db_connect)):
        user = db.query(Users).filter(Users.id == id).first()
        if not user:
             return {'User': None}
        new_task = Todo(
             task = task.task,
             status = task.status if task.status else False,
             user_id = id 
        )
        db.add(new_task)
        db.commit()
        return {
        'id': new_task.id,
        'task': new_task.task,
        'status': new_task.status,
        'user_id': new_task.user_id
    }


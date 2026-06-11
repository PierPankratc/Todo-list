from fastapi import FastAPI
import uvicorn 
from api.routers import users

app = FastAPI()

app.include_router(users.router)

if __name__ == '__main__':
    uvicorn.run(app='main:app', reload = True)

from fastapi import FastAPI
import uvicorn 
from api.routers import users, auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)


if __name__ == '__main__':
    uvicorn.run(app='main:app', reload = True)

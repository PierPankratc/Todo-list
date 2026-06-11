from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    name: str
    model_config = {'extra': 'forbid'}

class TaskSchema(BaseModel):
    task: str
    status: bool = Field(default=False)
    model_config = {'extra': 'forbid'}                                                            


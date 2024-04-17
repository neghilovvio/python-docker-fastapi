from pydantic import BaseModel, validator
from typing import List, Optional

class User(BaseModel):
    name: str
    age: int
    email: str
    friends: List[str] = []
    nickname: Optional[str] = 'Username'

    @validator('age')
    def validate_age(cls, value):
        if value < 0:
            raise ValueError('Age must be a positive integer')
        return value

    @validator('email')
    def validate_email(cls, value):
        if '@' not in value:
            raise ValueError('Invalid email address provided')
        return value.lower()



data = {
    'name': '2',
    'age': -10,
    'email': 'johndoe@example.com',
    'friends': ['Jane Doe', 'Richard Roe']
}



user_data = User(**data)


def myfunction(user_data: User):
    print(user_data)


myfunction(user_data)

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import  List


app = FastAPI()


# DB CONNECTION


SQLALCHEMY_DATABASE_URL = "postgresql://user:password@db/fastapi"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# TABLES


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(String)


class Business(Base):
    __tablename__ = "business"

    id = Column(Integer, primary_key=True, index=True)
    business_name = Column(String, index=True)
    address = Column(String, index=True)


# SCHEMA


class UserSchema(BaseModel):
    name: str
    age: int

    class Config:
        orm_mode = True

class UserWithIdSchema(UserSchema):
    id: str



@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine) 


# <----- APIS -----> #



# GET

@app.get("/users/{user_id}", response_model=List[UserWithIdSchema])
def read_users(user_id: int, db: SessionLocal = Depends(get_db)):
    results = db.query(User).filter(User.id == user_id).all()
    return results



# POST

@app.post("/users/", response_model=UserSchema, status_code=201)
def create_user(user: UserSchema, db: SessionLocal = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# PUT

# DELETE




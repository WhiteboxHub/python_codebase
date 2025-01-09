# from fastapi import FastAPI
# from pydantic import BaseModel
# from datetime import date

# # Initialize FastAPI app
# app = FastAPI()

# # Define Pydantic model for the request body
# class User(BaseModel):
#     name: str
#     age: int
#     signup_date: date

# # Define a route to handle user registration
# @app.post("/register/")
# async def register_user(user: User):
#     # You can now access validated user data
#     return {
#         "message": f"User {user.name} registered successfully!",
#         "user": user  # This will automatically return the User data as JSON
#     }

# # Define a route to return a list of users
# @app.get("/users/")
# async def get_users():
#     return [
#         {"name": "rahul", "age": 30, "signup_date": "2023-12-01"},
#         {"name": "Bob", "age": 24, "signup_date": "2024-01-15"}
#     ]







# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from datetime import date
# from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.future import select
# from databases import Database

# # Initialize FastAPI app
# app = FastAPI()

# # PostgreSQL database URL (update with your credentials)
# DATABASE_URL = "postgresql://postgres:0143@localhost:5432/postgres"

# # Initialize Database instance
# database = Database(DATABASE_URL)

# # SQLAlchemy setup
# Base = declarative_base()

# # Define the users table
# class UserTable(Base):
#     __tablename__ = "data validation"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     age = Column(Integer)
#     birthdate = Column(Integer)
#     fnumbers =Column(Integer)

# # Create a SQLAlchemy engine and session
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Create tables in the database
# Base.metadata.create_all(bind=engine)

# # Define Pydantic model for the request body
# class User(BaseModel):
#     name: str
#     age: int
#     birthdate: date
#     fnumbers: int


# # Define a route to handle user registration
# @app.post("/register/")
# async def register_user(user: User):
#     query = UserTable.__table__.insert().values(name=user.name, age=user.age, birthdate=user.birthdate,fnumbers=user.fnumbers)
#     last_record_id = await database.execute(query)
#     return {"message": f"User {user.name} registered successfully!", "user_id": last_record_id}

# # Define a route to return a list of users
# @app.get("/users/")
# async def get_users():
#     query = select(UserTable)
#     users = await database.fetch_all(query)
#     return users







from fastapi import FastAPI, HTTPException
from pydantic import BaseModel #data validation 
from datetime import date
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from databases import Database

# Initialize FastAPI app
app = FastAPI()

# PostgreSQL database URL (update with your credentials)
DATABASE_URL = "postgresql://postgres:0143@localhost:5432/postgres"

# Initialize Database instance
database = Database(DATABASE_URL)

# SQLAlchemy setup
Base = declarative_base()

# Define the users table
class UserTable(Base):
    __tablename__ = "data_validation"  # Updated table name to avoid spaces
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    birthdate = Column(Date)  # Changed to Date type
    fnumbers = Column(Integer)

# Create a SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Define Pydantic model for the request body
class User(BaseModel):
    name: str
    age: int
    birthdate: date  # Ensure date type matches Pydantic and SQLAlchemy
    fnumbers: int

# Connect to the database when the app starts
@app.on_event("startup")
async def startup():
    await database.connect()

# Disconnect from the database when the app shuts down
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Define a route to handle user registration
@app.post("/register/")
async def register_user(user: User):
    query = UserTable.__table__.insert().values(
        name=user.name, 
        age=user.age, 
        birthdate=user.birthdate,  # Pydantic's date matches SQLAlchemy's Date
        fnumbers=user.fnumbers
    )
    last_record_id = await database.execute(query)
    return {"message": f"User {user.name} registered successfully!", "user_id": last_record_id}

# Define a route to return a list of users
@app.get("/users/")
async def get_users():
    query = select(UserTable)
    users = await database.fetch_all(query)
    return users

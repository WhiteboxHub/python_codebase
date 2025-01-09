from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    name: str
    birthdate: date  
    age: int         
    favorite_numbers: list[int] 

# Example data where types are not exactly what we expect
user_data = {
    "name": "Rahul",
    "birthdate": "1995-07-16",   
    "age": "29",  
    "favorite_numbers": ["1", "42", "7"]  
}

user = User(**user_data)

print(user)
print(user.birthdate, type(user.birthdate))
print(user.age, type(user.age))              
print(user.favorite_numbers, type(user.favorite_numbers[0]))  

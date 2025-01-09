from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    name: str
    age: int
    signup_date: date

# Creating an instance of the model
user = User(name="rahul", age=25, signup_date="2023-12-15")

# Convert to a dictionary using `.dict()`
# user_dict = user.dict()
# print("Dictionary:", user_dict)

# Convert to JSON using `.json()`
user_json = user.json()
print("JSON:", user_json)

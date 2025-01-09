from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr 
    age: int

# Valid data
# user = User(name="John Doe", email="john@example.com", age=25)
# print(user)


#incorrect data
user = User(name="John Doe", email="not-an-email", age="twenty-five")
print(user)




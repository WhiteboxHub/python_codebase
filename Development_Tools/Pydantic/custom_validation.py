from pydantic import BaseModel, validator, ValidationError

class User(BaseModel):
    name: str
    age: int
    password: str
    
    # Custom validator for the `age` field
    @validator('age')
    def check_age(cls, value):
        if value < 18:
            raise ValueError('Age must be 18 or older')
        return value
    
    # Custom validator for the `password` field
    @validator('password')
    def check_password_length(cls, value):
        if len(value) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return value

# Example of valid input
# try:
#     user = User(name="John", age=20, password="strongpass")
#     print(user)
# except ValidationError as e:
#     print(e)

# Example of invalid input (age < 18 and password too short)
try:
    user = User(name="Jane", age=16, password="short")
except ValidationError as e:
    print(e)

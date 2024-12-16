# Local and global scope
x = "global"

def my_function():
    x = "local"
    print("Inside function:", x)

my_function()
print("Outside function:", x)

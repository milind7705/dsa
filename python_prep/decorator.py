from functools import wraps


# def my_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print("In wrapper")
#         return func(*args, **kwargs)
#     return wrapper
#
# @my_decorator
# def my_function():
#     print("This is normal function")
#
# my_function()

# Decorator with argument

def audit_log(level=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("LOG LEVEL", level)
            return func(*args, **kwargs)
        return wrapper
    return decorator



@audit_log(level="CODE")
def my_function():
    print("Inside my function")

my_function()

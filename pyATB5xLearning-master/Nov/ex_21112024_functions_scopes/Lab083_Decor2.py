def decorator1(func):
    def wrapper():
        print("start 1")
        func()
        print("end 1")
    return wrapper

def decorator2(func):
    def wrapper():
        print("start 2")
        func()
        print("end 2")
    return wrapper


@decorator1
@decorator2
def say_hello():
    print("Hello!")


say_hello()
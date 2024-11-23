def dec1(func):
    def wrapper():
        print("start")
        func()
        print("end")

    return wrapper


def dec2(func):
    def wrapper():
        print("start logging")
        func()
        print("end logging")

    return wrapper


@dec1
@dec2
def test():
    print("b1")
@dec1
@dec2
def test2():
    print("b2")


test()
test2()

def add_security(func):

    def wrapper():
        print("1.Before the function is called.")
        func() # # driving_scooty()
        print("3.After the function is called.")

    return wrapper()

@add_security
def drive_ola_scooter():
    print("ola")



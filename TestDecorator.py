def new_decoratore(func):
    def new_Warpper(*args,**kwargs):

        print("Befor Run Method")
        func(*args,**kwargs)
        print("After Run Method")

    return new_Warpper


@new_decoratore
def WriteName(name):
    return print(f"Hello {name}")
@new_decoratore
def Age(age):
    return print(f"Your Age {age}")

# Calling Functions
WriteName("Juhaina")
Age(25)
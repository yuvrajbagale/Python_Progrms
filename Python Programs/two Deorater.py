def decor(func):
    def inner(name):
        print("First Decor(Decor) fucntion Exections")
        func(name)
    return inner

def decor1(func):
    def inner(name):
        print("Seccond Decor(Decor1) Execution")
        func(name)
    return inner

@decor1
@decor
def wish(name):
    print("hello",name,"good morning")

wish("yuvraj")
def diwali(func):
    def inner(name):
        if name=='Akshay':
            print("Diwali is Awosaome.....")
        else:
            func(name)
    return inner
@diwali
def wish(name):
    print("Happy Diwali",name,"Stay Safe")
wish("Akshay")
wish("Yuvraj")

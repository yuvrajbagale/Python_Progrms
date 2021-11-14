def decor(func):
    def inner(name):
        if name=='sunny':
            print("Bad Morning")
        else:
            func(name)
    return inner

def wish(name):
    print('Good Moning',name)

decorfunction=decor(wish)

wish('sunny')
decorfunction('sunny')
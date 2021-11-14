def smart_division(func):
    def inner(a,b):
        if b==0:
            print("hello stupid ... How we can divide with zero")
            
        else:
            return func(a,b)
    return inner

@smart_division
def division(a,b):
    return a/b

print(division(20,2))
print(division(10,2))

print(division(50,2))
print(division(10, 0))
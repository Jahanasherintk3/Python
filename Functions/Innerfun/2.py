def outer():
    def inner():
        print("inner")
    return inner
x=outer()
print(x())


a=10
def add():
    pass
print(id(a))
print(id(add))


#Dekorator dekoruje naszą fukncję o jakies zachowania, np. że b edzie pisana z dużej litery itd.

def uppercase_decorator(function):

    def wrap():
        text = function()
        return text.upper()

    return wrap

def hello_world():
    return 'hello world'

decorator = uppercase_decorator(hello_world)
print(decorator())


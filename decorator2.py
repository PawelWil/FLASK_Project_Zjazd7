def plus_one(number):
    def add_one(n):
        return  n + 1

    return add_one(number)


print(plus_one(5))


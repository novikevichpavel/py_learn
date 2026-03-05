mult = lambda a, b: a * b
print(mult(5, 5))


def greeting(greet):
    return lambda name: f"{greet}, {name}"

morning_greet = greeting("Good morning")

print(morning_greet("Pavel"))
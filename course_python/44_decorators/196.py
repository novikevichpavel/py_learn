# Декораторы это специальные функции, которые выполняют другие фукнции автоматически


def decorator_func(orig_fn):
    def warpper(a, b):
        result = orig_fn(a, b)
        return result
    
    return warpper

@decorator_func
def my_fn(a, b): # Теперь эта функция передается в функцию decarator_func
    print("This is my func")
    return (a, b)

result = my_fn(5, 10)
print(result)
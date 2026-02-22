my_disk = {}

print(id(my_disk))
print(type(my_disk))

my_disk['brand'] = 'Samsung'
my_disk['price'] = 80

print(my_disk)

print(my_disk.items()) # Возвращает список кортежей, разбивая ключ-значение на каждый кортеж

print(my_disk.keys()) # Вернут только ключи в виде списка. С помощью функции list() можно целиком преобразовать в словарь
# Для получения значения из словаря используются []
my_bike = {
    'brand': 'BMW',
    'price': 29000,
    'engine_vol': 2.0
}

print(my_bike['price'])

# Изменение значений происходит также при использовании []
my_bike['price'] = 25000
print(my_bike)

# Таким же образом происходит добавление элементов
my_bike['aplicability'] = True
print(my_bike)

# Для удаление элемнетов используется операторв del
del my_bike['engine_vol']
print(my_bike)
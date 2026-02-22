# При повытке получения несуществующего ключа - будет получена получена ошибка ключа

new_bike = {
    'brand': 'BMW',
    'engine_vol': 2.2,
    'price': 30700,
    'bike_info': {
        'manufacaturer_country': 'Germany',
        'manufacturer': 'Bayrische Motor Werke',
        'is_available': True
    }
}
#print(new_bike['country'])

# Для избежания ошибок, и если нет уверенности, что такой ключ есть в словаре можно использовать метод get(). Будет возращен None, если такого ключа нет и выполнение кода продолжится

print(new_bike.get('country'))

# Также можно изменять возвращаемое значение6 если нет ключа, например, возращать 0 вместо None

print(new_bike.get('model', 0))
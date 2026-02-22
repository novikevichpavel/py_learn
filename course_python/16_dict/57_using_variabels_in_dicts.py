# Доступ к значение элемента через переменную

my_bike = {
    'brand': 'Ducati',
    'price': 27000,
    'engine_vol': 2.0
}
key_name = 'brand'
my_bike[key_name] = 'Honda'
print(my_bike)

# Вложенные словари
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

print(new_bike['bike_info']['manufacturer'])


# Использвоание переменных
brand = 'Minsk'
price = 17000
engine_volume = 1.2

bel_bike = {
    'brand': brand,
    'price': price,
    'engine_vol': engine_volume
}
print(bel_bike)

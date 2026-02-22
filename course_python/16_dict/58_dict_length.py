# Для получения длины словаря используется встроенная функция len()

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
print(len(new_bike))
print(len(new_bike['bike_info']))
del new_bike['engine_vol']
print(len(new_bike))
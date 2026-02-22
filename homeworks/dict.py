# 1. Создать пустой словарь
# 2. Трижды потребовать ввод сначала ключа, а затем его значения. Всего должно быть 6 запросов на вводю
# 3. Во время получения данных от пользователя добавить в словарь ключисо значениями согласно тому, что ввел пользовтель.
# 4. Выведите резльтирующий словарь в терминал

# 1

my_dict = {}

k1 = input('Enter key one: ')
v1 = input('Enter value one: ')
my_dict[k1] = v1
k2 = input('Enter key two: ')
v2 = input('Enter value two: ')
my_dict[k2] = v2
k3 = input('Enter key three: ')
v3 = input('Enter value three: ')
my_dict[k3] = v3

print(my_dict)



# 2

new_dict = {}

for i in range(3):
    k = input('Enter key: ')
    v = input('Enter val: ')
    new_dict[k] = v

print(new_dict)

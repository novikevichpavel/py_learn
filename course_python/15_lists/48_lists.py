# Списки - упорядоченная последовательность элементов. Селодаветльное у каждого элемента есть свой индекс

my_fruits = ["banana", "apple", "lime"]
other_fruits = ["apple", "banana", "lime"]

print(my_fruits == other_fruits)
print(len(my_fruits)) # Длина списка

print(my_fruits[1]) # Получение значения с индексом 1
print(my_fruits[-1]) # Получение последнего значения. -2 Второй с конца и так далее

#  Изменение значений элементов в списке
my_fruits[0] = "Lord Woldemort"
print(my_fruits)


# Удаление элементов в списке
del other_fruits[1]
print(other_fruits)


# Списки словарей
users = [
    {
        "user_name": "Pavel",
        "user_surname": "Novikevich"
    },
    {
        "user_name": "Polina",
        "user_surname": "kazakevich"
    }
]

print(len(users)) # Длина списка
print(users[1]) # Доступ к элементу списка
print(users[1]["user_name"]) # Доступ к значение опредленного ключа


# Формирование списка из переменных
fruit_one = "Banana"
fruit_two = "Lime"
friut_three = "Apple"

my_fruits = [fruit_one, fruit_two, friut_three]
print(my_fruits)

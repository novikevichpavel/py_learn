# Методы списков 

# append - добавление элементов в список. Добавляет элемент в конец списка
names = []
names.append("Pavel")
names.append("Polina")
print(names)
names.append("Vladislav")
print(names)


# pop - удаление элементов из списка. Если не передавать аргумент - удаляет посленднийэлемент из списка
inputs = [True, 'Hello', 123, 10.5]
inputs.pop()
print(inputs)
inputs.pop(0)
print(inputs)


# sort - сортировка элементов списка. Пример если список содержит целые числа, вызывая метод sort список будет отсортирован по возрастанию, если не передавать аргументы. Если передавать аргумент reverse=True - список будет отсортирован по убыванию. То есть при вызове без аргумента парметр. reverse проставляется дефолтно со значением False.
ids = [654, 233, 888, 734, 111, 5434, 2356]
ids.sort()
print(ids)
ids.sort(reverse=False)
print(ids)
ids.sort(reverse=True)
print(ids)
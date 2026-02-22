# Копирование списков. Невозможно копировать список путем присванивания одного списка другому, в таком случае просто создается новая доп ссылка на списко, и при изменении значении в одной из переменной из менится общий объект.

# 1
cars = ["BMW", "Mercedes-Benz", "Renault"]
copied_cars = cars[:]
copied_cars.append("Audi")
print(cars)
print(copied_cars)

# 2 Предпочтительный
names = ["Pavel", "Polina"]
copied_names = names.copy()
copied_names.append("Oksana")
print(names)
print(copied_names)

# 3
fruits = ["banana", "apple"]
new_fruits = list(fruits)
new_fruits.append("lime")
print(fruits)
print(new_fruits)

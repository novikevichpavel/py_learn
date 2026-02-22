# Конвертация в список
greeting = "hello from Python!"
greeting_list = list(greeting)
print(greeting_list)

ratings = [2.5, 2.11, 3.55, 17.21]

print(min(ratings))
print(max(ratings))
print(sum(ratings))
print(sum(ratings) / len(ratings))


# Объединение списков
new_ratings = [555.55, 666.66]

old_new_ratings = ratings + new_ratings
print(old_new_ratings)


# Нарезка списков 
my_nums = [2.5, 5.0, 4.3, 3.7, 4.5]

first_two = my_nums[0:2] # Первые два элемента
print(first_two)

middle_val = my_nums[1:-1] # Все элементы исключая первый и последний
print(middle_val)

last_two = my_nums[-2:] # Два последних элемента
print(last_two)
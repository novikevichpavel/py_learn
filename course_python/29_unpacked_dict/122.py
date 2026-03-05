# 1

dict_one = {
    "width": 122,
    "heigh": 15
}

dict_two = {
    **dict_one, # Распаковывает первый внутри второго, то есть придает значения первого словаря второму
    "color": "red"
}

print(dict_two)



# 2

button_info = {
    "info": 122
}

button_style = {
    "color": "red",
    "size": 12
}

new_button = button_info | button_style

print(new_button)
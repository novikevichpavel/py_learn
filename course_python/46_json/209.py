import json

json_file = '{' \
    '"num_one": "number one",' \
    '"num_two": "number two"' \
    '}'

convert_json_to_dict = json.loads(json_file) # Конвертация json в словарь

print(convert_json_to_dict)
print(convert_json_to_dict["num_one"])
print(type(convert_json_to_dict))


new_dict = {
    "brand": "BMW",
    "engine_vol": 1.6,
    "price": 6000,
    "is_red_price": True
}

converted_dict = json.dumps(new_dict, indent=1) # Конвертация словаря в json с его редактирование для вывода в столбец
print(converted_dict)
print(type(converted_dict))
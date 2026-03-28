import json

my_dict = {
    "brand": "BMW",
    "model": "m5",
    "engine_parameters": {
        "engine_volume": 5.0,
        "engine_type": "v8"
    },
    "stock": 15,
    "is_red_price": False
}

converted_dict_to_send_db = json.dumps(my_dict, indent=4)

print(converted_dict_to_send_db)
print(type(converted_dict_to_send_db))
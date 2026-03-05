my_dict = {
    "a": 1,
    "b": 4,
    "c": 6
}

del my_dict["a"]

my_dict.__delitem__('b')

print(my_dict)

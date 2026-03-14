# 1


my_dict = {
    
    "name": "Pavel",
    "age": 27,
    "born_at": 1999
    
}

def dict_to_list(dict):
    dict_copy = dict.copy()

    for key in dict_copy:
        if isinstance(dict_copy[key], int):
            dict_copy[key] *= 2
            my_list = list(dict_copy.items())
            
    return my_list

print(dict_to_list(my_dict)) 




# 2


def filter_list(list, type_val):
    new_list = []
    for i in list:
        if type(i) is type_val:
            new_list.append(i)
    return new_list

print(filter_list(["a", 3, 6, 8, 11, True], int))



def list_to_filter(lst, value_type):
    def check_elem_value(elem):
        return isinstance(elem, value_type)
    
    return list(filter(check_elem_value, lst))

print(list_to_filter(["a", 3, 6, 8, 11, True], int))
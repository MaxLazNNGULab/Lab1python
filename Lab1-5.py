def max_dct(*dicts):
    merged_dict = {}
    for current_dict in dicts:
        for key, value in current_dict.items():
            if key in merged_dict:
                if value > merged_dict[key]:
                    merged_dict[key] = value
            else:
                merged_dict[key] = value
    return merged_dict

def sum_dct(*dicts):
    merged_dict = {}
    for current_dict in dicts:
        for key, value in current_dict.items():
            if key in merged_dict:
                merged_dict[key] += value
            else:
                merged_dict[key] = value
    return merged_dict

dict1 = {'a': 5, 'b': 10}
dict2 = {'a': 9, 'c': 3}

print("max_dct result:", max_dct(dict1, dict2))
print("sum_dct result:", sum_dct(dict1, dict2))
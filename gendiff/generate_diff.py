#!usr/bin/env python3
import json


def get_diff_dict(dict1, dict2):
    keys = set(dict1) | set(dict2)
    sorted_keys = list(sorted(keys))
    new_dict = {}
    for key in sorted_keys:
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                new_dict["   " + key] = dict1[key]
            elif dict1[key] != dict2[key]:
                new_dict[" - " + key] = dict1[key]
                new_dict[" + " + key] = dict2[key]
        elif key in dict1 or key in dict2:
            if key in dict1:
                new_dict[" - " + key] = dict1[key]
            elif key in dict2:
                new_dict[" + " + key] = dict2[key]
    return new_dict


def generate_diff(filepath1, filepath2):
    dict1 = json.load(open(filepath1))
    dict2 = json.load(open(filepath2))
    diff_dict = get_diff_dict(dict1, dict2)
    string = json.dumps(diff_dict)
    no_quotes_commas = string.replace('"', "").replace(",", "\n")
    diff_string = no_quotes_commas.replace("{", "{\n ").replace("}", "\n}")
    return diff_string

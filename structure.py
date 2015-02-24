#!/usr/bin/env python

"""
Desc:
    type_test(data, structure)
    arg data - variable to verify
    arg structure - variable used to verify data

    If equal in structure it returns True

Author: David Robertsson
Email: david.robertsson@gmail.com
"""

def dict_test(data, structure):
    """ Takes variable dict type and compares it with structure.
    If data is built as the structure, the function returns True
    else False
    """
    if type(data) is type(structure):
        for structure_key, structure_type in structure.items():
            if structure_key in data:
                if not type_test(data[structure_key], structure_type):
                    return False
            else:
                return False
        return True
    else:
        return False


def list_test(data, structure):
    """  Takes variable list type and compares it with structure.
    If data is built as the structure, the function returns True
    else False
    """
    for data_field, structure_field in zip(data, structure):
        if not type_test(data_field, structure_field):
            return False
    if type(data) is type(structure) and (len(data) == len(structure)):
        return True
    else:
        return False


def type_test(data, structure):
    """ type_test() takes two input parameters.
    data - variable we want to verify
    structure - variable that dictates how the data variable should look like

    type_test is only able to verify basic types such float, int, str, unicode,
    dict and list. types such as tuples haven't been tested yet.

    If data and structure is equal in structure, type test will return True
    else False

    Example:
        data_a = [{'nyckel': 1}, 1, 2, 'three', 4]
        structure_a = [{'nyckel': int}, int, int, int, int]

        data_b = {'key': [1, 'string', 3], 'key2': {'key3': 1}}
        structure_b = {'key': [int, str, int], 'key2': {'key3': int}}

        case a: Will return False
        case b: Will return True
    """

    if type(data) is list:
        # LIST CASE
        # Check every element in a list, if list of structure and data is equal
        # Then finaly check if the lists is equal in size.
        return list_test(data, structure)
    elif type(data) is dict:
        # DICT CASE
        # Checks every key in structure against data. If equal, returns True
        return dict_test(data, structure)
    else:
        # Basic type case.
        if type(data) is structure:
            return True
        else:
            return False


if __name__ == '__main__':
    data_a = [{'nyckel': 1}, 1, 2, 'three', 4]
    structure_a = [{'nyckel': int}, int, int, int, int]

    data_b = {'key': [1, 'string', 3], 'key2': {'key3': 1}}
    structure_b = {'key': [int, str, int], 'key2': {'key3': int}}

    print(type_test(data_a, structure_a))
    print(type_test(data_b, structure_b))

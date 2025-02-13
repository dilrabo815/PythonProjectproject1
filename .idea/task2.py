def typeBasedTransformer(**kwargs):
    transformed = {}
    for key, value in kwargs.items():
        if type(value) == int or type(value) == float:
            transformed[key] = value *value
        elif type(value) == str:
            transformed[key] = value[::-1]
        elif type(value) == bool:
            transformed[key] = not value
        elif type(value) == list or type(value) == tuple:
            transformed[key] = value[::-1]
        elif type(value) == dict:
            reversed_dict = {}
            for k, v in value.items():
                reversed_dict[v] = k
            transformed[key] = reversed_dict

        else:
            transformed[key] = value
    return transformed

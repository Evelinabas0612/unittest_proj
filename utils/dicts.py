# файл dicts.py
def get_val(collection, key, default='git'):
    if len(collection) == 0:
        return default
    elif key not in collection:
        return default
    elif collection[key] is None:
        return "Значение None"

    return collection[key]


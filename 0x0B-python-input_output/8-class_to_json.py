#!/usr/bin/python3
def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization.

    Only attributes that are serializable (list, dict, str, int, bool)
    will be included in the returned dictionary.
    """
    return {
        key: value
        for key, value in obj.__dict__.items()
        if isinstance(value, (list, dict, str, int, bool))
    }

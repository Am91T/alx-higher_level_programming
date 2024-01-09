def class_to_json(obj):
    """Converts a class instance to a JSON-serializable dictionary."""
    result = {}

    # Iterate over the attributes of the object
    for attr_name, attr_value in obj.__dict__.items():
        # Check if the attribute is a simple data type
        if isinstance(attr_value, (int, str, bool, list, dict)):
            result[attr_name] = attr_value

    return result

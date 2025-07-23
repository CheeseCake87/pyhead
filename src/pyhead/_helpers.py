def has_key(element):
    if hasattr(element, "key"):
        if element.key:
            return element.key

    return None

from string import punctuation, whitespace


def has_key(element):
    if hasattr(element, "key"):
        if element.key:
            return element.key

    return None


def replace_special_chars(value: str):
    """
    Replace special characters in a string.

    Returns:
        str: String with special characters replaced.
    """
    special_chars = [punctuation, whitespace]
    for special_char in special_chars:
        value = value.replace(special_char, "-")
    return value

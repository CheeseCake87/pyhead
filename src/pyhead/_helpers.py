from hashlib import md5
from random import choices
from string import ascii_letters, digits, punctuation, whitespace
from typing import Union, Optional


def has_key(element):
    if hasattr(element, "key"):
        if element.key:
            return element.key

    return None


def random_key(append: Optional[Union[str, int]] = None) -> str:
    """
    Generate a random string used in element keys.

    Returns:
        str: Random string of given length.
    """
    return (
        "".join(choices(ascii_letters + digits, k=12)) + str(append)
        if append
        else "".join(choices(ascii_letters + digits, k=12))
    )


def generate_script_tag_lookup_id(src: str) -> str:
    """
    Generate a unique lookup id for a script tag.

    Returns:
        str: Unique lookup id for a script tag.
        :param dict_length:
        :param src:
    """
    squish = replace_special_chars(src)
    randomised = md5(squish.encode()).hexdigest()
    return randomised


def generate_stylesheet_tag_lookup_id(href: str) -> str:
    """
    Generate a unique lookup id for a stylesheet tag.

    Returns:
        str: Unique lookup id for a stylesheet tag.
    """
    squish = replace_special_chars(href)
    randomised = md5(squish.encode()).hexdigest()
    return randomised


def generate_meta_tag_lookup_id(
    name: Optional[str],
    http_equiv: Optional[str],
    property_: Optional[str],
    content: Optional[str],
) -> str:
    """
    Generate a unique lookup id for a meta tag.

    Returns:
        str: Unique lookup id for a meta tag.
        :param dict_length:
        :param name:
        :param content:
        :param property_:
        :param http_equiv:
    """
    collect = [name, http_equiv, property_, content]
    squish = "".join([replace_special_chars(str(i)) for i in collect if i])
    randomised = md5(squish.encode()).hexdigest()
    return randomised


def generate_link_tag_lookup_id(
    rel: str,
    href: Optional[str] = None,
    sizes: Optional[str] = None,
    type_: Optional[str] = None,
    hreflang: Optional[str] = None,
) -> str:
    """
    Generate a unique lookup id for a link tag.

    Returns:
        str: Unique lookup id for a link tag.
        :param dict_length:
        :param rel:
        :param hreflang:
        :param type_:
        :param sizes:
        :param href:
    """
    collect = [rel, href, sizes, type_, hreflang]
    squish = "".join([replace_special_chars(str(i)) for i in collect if i])
    randomised = md5(squish.encode()).hexdigest()
    return randomised


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

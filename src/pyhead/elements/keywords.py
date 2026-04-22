from typing import Optional

from markupsafe import escape

from .._base import BaseElement


class Keywords(BaseElement):
    key: str = "keywords"

    _keywords: list[str]

    def __init__(
        self, from_string: Optional[str] = None, from_list: Optional[list[str]] = None
    ) -> None:
        self._keywords = []

        if from_string is not None:
            self._keywords = from_string.split(",")

        if from_list is not None:
            self._keywords.extend(from_list)

    def __repr__(self) -> str:
        return f"Keywords(keywords={self._keywords!r})"

    def compile(self) -> str:
        join = ", ".join(self._keywords)
        return f'<meta name="keywords" content="{escape(join)}">'

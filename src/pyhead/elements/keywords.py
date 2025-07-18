from typing import Optional

from markupsafe import Markup


class Keywords:
    unique: bool = True
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
        return f'<Keywords page_keywords="{self._keywords}">'

    def __str__(self) -> Markup:
        return Markup(self._compile())

    def __call__(self) -> Markup:
        return Markup(self._compile())

    def _compile(self) -> str:
        join = ", ".join(self._keywords)
        return f'<meta name="keywords" content="{join}">'

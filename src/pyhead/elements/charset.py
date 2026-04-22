from markupsafe import escape

from .._base import BaseElement


class Charset(BaseElement):
    key: str = "charset"

    _charset: str

    def __init__(self, charset: str = "utf-8") -> None:
        self._charset = charset

    def __repr__(self) -> str:
        return f"Charset(charset={self._charset!r})"

    def compile(self) -> str:
        return f'<meta charset="{escape(self._charset)}">'

from typing import Optional

from markupsafe import Markup, escape


class Charset:
    key: str = "charset"

    _charset: Optional[str]

    def __init__(self, charset: str = "utf-8") -> None:
        self._charset = charset

    def __repr__(self) -> str:
        return f'<Charset charset="{self._charset}">'

    def __str__(self) -> Markup:
        return Markup(self.compile())

    def __call__(self) -> Markup:
        return Markup(self.compile())

    def compile(self) -> str:
        return f'<meta charset="{escape(self._charset)}">'

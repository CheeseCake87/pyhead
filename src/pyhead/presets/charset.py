from typing import Optional

from markupsafe import Markup


class Charset:
    charset: Optional[str]

    def __init__(self, charset: str = "utf-8") -> None:
        self.charset = charset

    def __repr__(self) -> str:
        return f'<Charset charset="{self.charset}">'

    def __str__(self) -> Markup:
        return Markup(self._compile())

    def __call__(self) -> Markup:
        return Markup(self._compile())

    def _compile(self) -> str:
        return f'<meta charset="{self.charset}">'

    def replace(self, charset: str) -> "Charset":
        self.charset = charset
        return self

from typing import Union

from markupsafe import Markup, escape

from ..protocols import CompileDelayed


class Base:
    unique: bool = True
    key: str = "base"

    _href: Union[str, CompileDelayed]

    def __init__(self, href: Union[str, CompileDelayed]) -> None:
        self._href = href

    def __repr__(self) -> str:
        return f'<Base base="{self._href}">'

    def __str__(self) -> Markup:
        return Markup(self.compile())

    def __call__(self) -> Markup:
        return Markup(self.compile())

    def compile(self) -> str:
        href = (
            self._href.compile()
            if isinstance(self._href, CompileDelayed)
            else self._href
        )
        return f'<base href="{escape(href)}">'

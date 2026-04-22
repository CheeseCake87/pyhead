from typing import Union

from markupsafe import escape

from .._base import BaseElement
from ..protocols import CompileDelayed


class Base(BaseElement):
    key: str = "base"

    _href: Union[str, CompileDelayed]

    def __init__(self, href: Union[str, CompileDelayed]) -> None:
        self._href = href

    def __repr__(self) -> str:
        return f"Base(href={self._href!r})"

    def compile(self) -> str:
        href = (
            self._href.compile()
            if isinstance(self._href, CompileDelayed)
            else self._href
        )
        return f'<base href="{escape(href)}">'

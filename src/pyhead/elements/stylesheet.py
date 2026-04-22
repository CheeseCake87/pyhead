from typing import Optional, Union

from .._base import BaseElement
from .link import Link
from ..protocols import CompileDelayed


class Stylesheet(BaseElement):
    _href: Union[str, CompileDelayed]
    _id: Optional[str]

    def __init__(
        self, href: Union[str, CompileDelayed], id_: Optional[str] = None
    ) -> None:
        self._href = href
        self._id = id_

        if id_:
            self.key = id_

    def __repr__(self) -> str:
        parts = [f"href={self._href!r}"]
        if self._id is not None:
            parts.append(f"id={self._id!r}")
        return f"Stylesheet({', '.join(parts)})"

    def compile(self) -> str:
        return str(Link(rel="stylesheet", href=self._href, id_=self._id))

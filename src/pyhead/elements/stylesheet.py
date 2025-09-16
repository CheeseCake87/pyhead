from typing import Optional, Union

from markupsafe import Markup

from .link import Link
from ..protocols import CompileDelayed


class Stylesheet:
    unique: bool = False
    key: str = None

    _href: Union[str, CompileDelayed]
    _id: Optional[str]

    def __init__(
        self, href: Union[str, CompileDelayed], id_: Optional[str] = None
    ) -> None:
        self.unique = False

        self._href = href
        self._id = id_

        if id_:
            self.key = id_

    def __repr__(self) -> str:
        return f"<Stylesheet href={self._href}>"

    def __str__(self) -> Markup:
        return Markup(self.compile())

    def __call__(self) -> Markup:
        return Markup(self.compile())

    def compile(self) -> str:
        stylesheet = Link(rel="stylesheet", href=self._href, id_=self._id)
        return str(stylesheet)

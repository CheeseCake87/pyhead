from typing import Optional

from markupsafe import Markup

from .link import Link


class Stylesheet:
    unique: bool = False
    key: str = None

    _href: str
    _id: Optional[str]

    def __init__(self, href: str, id_: Optional[str] = None) -> None:
        self.unique = False

        self._href = href
        self._id = id_

        if id_:
            self.key = id_

    def __repr__(self) -> str:
        return f"<Stylesheet href={self._href}>"

    def __str__(self) -> Markup:
        return Markup(self._compile())

    def __call__(self) -> Markup:
        return Markup(self._compile())

    def _compile(self) -> str:
        stylesheet = Link(rel="stylesheet", href=self._href, id_=self._id)
        return str(stylesheet)

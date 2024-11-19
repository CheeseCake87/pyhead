from typing import Optional

from markupsafe import Markup

from ..tags import LinkTag


class Stylesheet:
    href: str
    id_: Optional[str]

    def __init__(self, href: str, id_: Optional[str] = None) -> None:
        self.href = href
        self.id_ = id_

    def __repr__(self) -> str:
        return f"<Stylesheet href={self.href}>"

    def __str__(self) -> Markup:
        return Markup(self._compile())

    def __call__(self) -> Markup:
        return Markup(self._compile())

    def _compile(self) -> str:
        _ = LinkTag(rel="stylesheet", href=self.href, id_=self.id_)
        return str(_)

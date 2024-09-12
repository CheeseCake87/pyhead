from markupsafe import Markup

from ..tags import LinkTag


class Stylesheet:
    href: str

    def __init__(self, href: str) -> None:
        self.href = href

    def __repr__(self) -> str:
        return f"<Stylesheet href={self.href}>"

    def __str__(self) -> Markup:
        return Markup(self._compile())

    def __call__(self) -> Markup:
        return Markup(self._compile())

    def _compile(self) -> str:
        _ = LinkTag(rel="stylesheet", href=self.href)
        return str(_)

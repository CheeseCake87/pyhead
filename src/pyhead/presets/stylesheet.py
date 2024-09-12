from markupsafe import Markup

from ..tags import LinkTag


class Stylesheet:
    href: str

    def __init__(self, href: str):
        self.href = href

    def __repr__(self):
        return f"<Stylesheet href={self.href}>"

    def __str__(self):
        return Markup(self._compile())

    def __call__(self, *args, **kwargs):
        return Markup(self._compile())

    def _compile(self) -> Markup:
        return LinkTag(rel="stylesheet", href=self.href)()

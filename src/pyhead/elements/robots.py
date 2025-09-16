from markupsafe import Markup

from .meta import Meta


class Robots:
    unique: bool = True
    key: str = "robots"

    _content: str

    def __init__(self, content: str) -> None:
        self._content = content

    def __repr__(self) -> str:
        return f'<Robots content="{self._content}">'

    def __str__(self) -> Markup:
        return Markup(self.compile())

    def __call__(self) -> Markup:
        return Markup(self.compile())

    def compile(self) -> str:
        meta = Meta(name="robots", content=self._content)
        return str(meta)

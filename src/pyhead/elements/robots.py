from .._base import BaseElement
from .meta import Meta


class Robots(BaseElement):
    key: str = "robots"

    _content: str

    def __init__(self, content: str) -> None:
        self._content = content

    def __repr__(self) -> str:
        return f"Robots(content={self._content!r})"

    def compile(self) -> str:
        return str(Meta(name="robots", content=self._content))

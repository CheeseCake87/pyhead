from .._base import BaseElement
from .meta import Meta


class ThemeColor(BaseElement):
    key: str = "theme_color"

    _content: str

    def __init__(self, content: str) -> None:
        self._content = content

    def __repr__(self) -> str:
        return f"ThemeColor(content={self._content!r})"

    def compile(self) -> str:
        return str(Meta(name="theme-color", content=self._content))

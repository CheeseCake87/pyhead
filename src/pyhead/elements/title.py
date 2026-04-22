from markupsafe import escape

from .._base import BaseElement


class Title(BaseElement):
    key: str = "title"

    _title: str

    def __init__(self, title: str) -> None:
        self._title = title

    def __repr__(self) -> str:
        return f"Title(title={self._title!r})"

    def compile(self) -> str:
        return f"<title>{escape(self._title)}</title>"

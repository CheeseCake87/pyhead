from markupsafe import escape

from .._base import BaseElement


class Title(BaseElement):
    key: str = "title"

    title_: str

    def __init__(self, title: str) -> None:
        self.title_ = title

    def __repr__(self) -> str:
        return f"Title(title={self.title_!r})"

    def compile(self) -> str:
        return f"<title>{escape(self.title_)}</title>"

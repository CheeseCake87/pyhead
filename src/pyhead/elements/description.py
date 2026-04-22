from markupsafe import escape

from .._base import BaseElement


class Description(BaseElement):
    key: str = "description"

    _description: str

    def __init__(self, description: str) -> None:
        self._description = description

    def __repr__(self) -> str:
        return f"Description(description={self._description!r})"

    def compile(self) -> str:
        return f'<meta name="description" content="{escape(self._description)}">'

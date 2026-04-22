from .._base import BaseElement
from .meta import Meta


class ApplicationName(BaseElement):
    key: str = "application_name"

    _content: str

    def __init__(self, content: str) -> None:
        self._content = content

    def __repr__(self) -> str:
        return f"ApplicationName(content={self._content!r})"

    def compile(self) -> str:
        return str(Meta(name="application_name", content=self._content))
